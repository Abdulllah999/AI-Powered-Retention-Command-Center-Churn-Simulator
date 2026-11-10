"""Permission and history safeguards: all external commands are mocked."""
from types import SimpleNamespace
import pytest
import publish_portfolio as publish

def test_wrong_account_stops_before_writes(monkeypatch):
    calls=[]
    monkeypatch.setattr(publish,'api',lambda *a,**k: {'login':'another-user'})
    monkeypatch.setattr(publish,'command',lambda *a,**k: calls.append(a) or SimpleNamespace(stdout='',returncode=0))
    with pytest.raises(RuntimeError,match='Log in as'): publish.preflight()
    assert calls == [('git','--version')]

def test_restricted_app_credential_stops_before_writes(monkeypatch):
    calls=[]
    monkeypatch.setattr(publish,'api',lambda *a,**k: {'login':'Abdulllah999'})
    def fake(*a,**k):
        calls.append(a)
        return SimpleNamespace(stdout='HTTP/2 200\nX-OAuth-Scopes: \nX-Test: next-header\n\nAbdulllah999\n',returncode=0)
    monkeypatch.setattr(publish,'command',fake)
    with pytest.raises(RuntimeError,match='lacks repo/user'): publish.preflight()
    assert not any(a[:3]==('gh','auth','setup-git') for a in calls)

def project_commands(calls, existing_sha):
    def fake(*a,**k):
        calls.append(a)
        if a[:3]==('git','rev-parse','HEAD'): return SimpleNamespace(stdout='expected-sha\n')
        if a[:3]==('git','ls-remote','--heads'): return SimpleNamespace(stdout=existing_sha+'\trefs/heads/main\n')
        if a[:2]==('git','push'): raise AssertionError('Existing history must never be pushed over')
        return SimpleNamespace(stdout='')
    return fake

def test_different_destination_history_is_preserved(monkeypatch,tmp_path):
    calls=[]
    monkeypatch.setattr(publish,'command',project_commands(calls,'unrelated-sha'))
    monkeypatch.setattr(publish,'destination',lambda *a: {'clone_url':'https://github.com/Abdulllah999/example.git'})
    monkeypatch.setattr(publish,'set_metadata',lambda *a: pytest.fail('Metadata must not change after history mismatch'))
    with pytest.raises(RuntimeError,match='refusing to overwrite'):
        publish.publish_project('example',tmp_path/'example','description',[])
    assert not any(a[:2]==('git','push') for a in calls)

def test_matching_history_resumes_without_push(monkeypatch,tmp_path):
    calls=[];metadata=[]
    monkeypatch.setattr(publish,'command',project_commands(calls,'expected-sha'))
    monkeypatch.setattr(publish,'destination',lambda *a: {'clone_url':'https://github.com/Abdulllah999/example.git','html_url':'https://github.com/Abdulllah999/example'})
    monkeypatch.setattr(publish,'set_metadata',lambda *a: metadata.append(a))
    result=publish.publish_project('example',tmp_path/'example','description',['python'])
    assert result['sha']=='expected-sha' and len(metadata)==1
    assert not any(a[:2]==('git','push') for a in calls)
