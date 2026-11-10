#!/usr/bin/env python3
"""Create/populate Abdullah's portfolio using a personally authorized GitHub CLI.
Run on your own computer: python publish_portfolio.py
Requires official GitHub CLI, Git and Python 3.10+. No tokens are accepted here.
"""
from pathlib import Path
import base64
import json
import re
import subprocess
import sys
import tempfile

OWNER = 'Abdulllah999'
SOURCE = OWNER + '/AI-Powered-Retention-Command-Center-Churn-Simulator'
SETTINGS = {
 'interview-evidence-lab': ('Human-reviewed skill evidence and interview prompts from fictional resume text. New portfolio implementation.', ['python','flask','nlp','recruitment','portfolio']),
 'sentiment-baseline-lab': ('Reproducible three-class TF-IDF baseline with authored fixtures, holdout evaluation and abstention.', ['python','scikit-learn','sentiment-analysis','nlp','machine-learning']),
 'health-patterns-demo': ('Educational synthetic symptom-pattern ML API and web demo with Flutter companion source. Not a diagnostic tool.', ['python','flask','machine-learning','synthetic-data','flutter']),
 'market-forecast-lab': ('Walk-forward forecasting with synthetic sentiment, price-only ablation and persistence baseline.', ['python','flask','time-series','forecasting','model-evaluation']),
}

def command(*args, cwd=None, stdin=None, check=True):
    result = subprocess.run(args, cwd=cwd, input=stdin, capture_output=True, text=True)
    if check and result.returncode:
        # Commands never carry tokens. GitHub CLI obtains credentials itself.
        raise RuntimeError(' '.join(args[:3]) + ' failed: ' + result.stderr.strip()[-1200:])
    return result

def api(endpoint, method='GET', data=None, check=True):
    args = ['gh', 'api', '--method', method, endpoint]
    if data is not None: args += ['--input', '-']
    result = command(*args, stdin=json.dumps(data) if data is not None else None, check=check)
    if not check: return result
    return json.loads(result.stdout) if result.stdout.strip() else {}

def preflight():
    command('git', '--version')
    user = api('user')
    if user.get('login','').lower() != OWNER.lower():
        raise RuntimeError('Log in as ' + OWNER + ' before running this script.')
    response = command('gh','api','--include','user','--jq','.login').stdout
    match = re.search(r'^x-oauth-scopes:[ \t]*([^\r\n]*)', response, re.I|re.M)
    scopes = set(s.strip() for s in match.group(1).split(',')) if match else set()
    if not {'repo','user'} <= scopes:
        raise RuntimeError('The effective API credential lacks repo/user OAuth scopes. Run this on your own computer after: gh auth login --hostname github.com --web --git-protocol https --scopes repo,workflow,user. The managed ChatGPT workspace continued to send requests as its restricted GitHub app even after CLI authorization.')
    command('gh','auth','setup-git')
    return user

def destination(name, description):
    result = api(f'repos/{OWNER}/{name}', check=False)
    if result.returncode:
        if '404' not in result.stderr:
            raise RuntimeError('Cannot check repository ' + name + ': ' + result.stderr[-600:])
        return api('user/repos','POST',{'name':name,'private':False,'auto_init':False,'description':description})
    repo = json.loads(result.stdout)
    if repo.get('private') or repo.get('archived') or repo.get('disabled'):
        raise RuntimeError('Will not change visibility or status of existing repository ' + name)
    return repo

def set_metadata(name, description, topics):
    api(f'repos/{OWNER}/{name}','PATCH',{'description':description,'default_branch':'main'})
    current = api(f'repos/{OWNER}/{name}/topics').get('names',[])
    api(f'repos/{OWNER}/{name}/topics','PUT',{'names':sorted(set(current)|set(topics))})

def publish_project(name, folder, description, topics):
    command('git','clone','--single-branch','--branch','portfolio/'+name,'https://github.com/'+SOURCE+'.git',str(folder))
    local_sha = command('git','rev-parse','HEAD',cwd=folder).stdout.strip()
    repo = destination(name,description)
    heads = command('git','ls-remote','--heads',repo['clone_url']).stdout.splitlines()
    main = [line.split()[0] for line in heads if line.endswith('refs/heads/main')]
    if heads and main != [local_sha]:
        raise RuntimeError('Existing repository contains different history; refusing to overwrite: '+name)
    if not heads:
        command('git','push',repo['clone_url'],'HEAD:refs/heads/main',cwd=folder)
    set_metadata(name,description,topics)
    print('Published '+repo['html_url'],flush=True)
    return {'url':repo['html_url'],'sha':local_sha}

def publish_profile(folder, user):
    draft = api(f'repos/{SOURCE}/contents/PROFILE-README-DRAFT.md')
    text = base64.b64decode(draft['content']).decode('utf-8')
    repo = destination(OWNER,'Abdullah Shakeel | Data science, AI and Python portfolio.')
    heads = command('git','ls-remote','--heads',repo['clone_url']).stdout.splitlines()
    if heads:
        current = api(f'repos/{OWNER}/{OWNER}/contents/README.md')
        if base64.b64decode(current['content']).decode('utf-8') != text:
            raise RuntimeError('Existing profile README differs; refusing to overwrite it.')
    else:
        folder.mkdir()
        (folder/'README.md').write_text(text,encoding='utf-8')
        command('git','init','-b','main',cwd=folder)
        command('git','config','user.name','Abdullah Shakeel',cwd=folder)
        command('git','config','user.email',str(user['id'])+'+'+OWNER+'@users.noreply.github.com',cwd=folder)
        command('git','add','README.md',cwd=folder)
        command('git','commit','-m','Add professional data science and AI profile',cwd=folder)
        command('git','push',repo['clone_url'],'HEAD:refs/heads/main',cwd=folder)
    set_metadata(OWNER,'Abdullah Shakeel | Data science, AI and Python portfolio.',['portfolio','data-science','python','machine-learning'])
    print('Published profile '+repo['html_url'],flush=True)
    return {'url':repo['html_url']}

def update_overview():
    file = api(f'repos/{SOURCE}/contents/PORTFOLIO.md')
    text = base64.b64decode(file['content']).decode('utf-8')
    updated = '\n'.join(line for line in text.split('\n') if not line.startswith('> Portfolio preview:'))
    for name in SETTINGS:
        updated = updated.replace('https://github.com/'+SOURCE+'/tree/portfolio/'+name,'https://github.com/'+OWNER+'/'+name)
        updated = updated.replace('https://raw.githubusercontent.com/'+SOURCE+'/portfolio/'+name+'/', 'https://raw.githubusercontent.com/'+OWNER+'/'+name+'/main/')
    if updated != text:
        api(f'repos/{SOURCE}/contents/PORTFOLIO.md','PUT',{'message':'Link individual project repositories from portfolio overview','sha':file['sha'],'content':base64.b64encode(updated.encode()).decode()})

def main():
    user = preflight()
    results = {}
    with tempfile.TemporaryDirectory(prefix='abdullah-portfolio-') as temp:
        temp = Path(temp)
        for name,(description,topics) in SETTINGS.items():
            results[name] = publish_project(name,temp/name,description,topics)
        results[OWNER] = publish_profile(temp/'profile',user)
    api('user','PATCH',{'name':'Abdullah Shakeel','location':'Islamabad, Pakistan','bio':'Data science & AI | Python, SQL & ML | Building reproducible models and useful data applications | Islamabad, Pakistan'})
    set_metadata(SOURCE.split('/',1)[1], 'Interactive Streamlit dashboard for synthetic customer-risk scenarios, with reproducible evaluation and explicit baselines. Educational portfolio demo.', ['python','streamlit','scikit-learn','plotly','data-science','synthetic-data','model-evaluation','dashboard'])
    update_overview()
    print(json.dumps(results,indent=2))
    print('Done. On your GitHub profile, use Customize your pins to select the five project repositories. Check Actions for each new repository before claiming its CI passed.')

if __name__ == '__main__':
    try: main()
    except (RuntimeError,FileNotFoundError) as exc:
        print('Stopped safely: '+str(exc),file=sys.stderr)
        sys.exit(1)
