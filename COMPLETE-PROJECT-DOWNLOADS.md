# Project source downloads and publication

All four new implementations are fully available as source, not just README drafts. These ZIPs include application code, pinned direct dependencies, example data, tests, CI configuration, local screenshots and evaluation output.

| Project | Complete source ZIP | Implemented scope |
| --- | --- | --- |
| Interview Evidence Lab | [Download ZIP](https://codeload.github.com/Abdulllah999/AI-Powered-Retention-Command-Center-Churn-Simulator/zip/refs/heads/portfolio/interview-evidence-lab) | Working Flask text skill-evidence and interview-prompt prototype; no candidate ranking, personality or emotion inference |
| Sentiment Baseline Lab | [Download ZIP](https://codeload.github.com/Abdulllah999/AI-Powered-Retention-Command-Center-Churn-Simulator/zip/refs/heads/portfolio/sentiment-baseline-lab) | Working three-class TF-IDF/logistic-regression web demo, authored fixtures, holdout and baseline |
| Health Pattern Explorer | [Download ZIP](https://codeload.github.com/Abdulllah999/AI-Powered-Retention-Command-Center-Churn-Simulator/zip/refs/heads/portfolio/health-patterns-demo) | Working synthetic ML Flask web/API demo and fixed FAQ; Flutter companion source is not built or validated |
| Market Forecast Lab | [Download ZIP](https://codeload.github.com/Abdulllah999/AI-Powered-Retention-Command-Center-Churn-Simulator/zip/refs/heads/portfolio/market-forecast-lab) | Working synthetic next-close forecasting web demo with expanding-window evaluation, sentiment ablation and persistence baseline |

These are new portfolio implementations, not recovered CV project code or reproductions of every original feature. Authored/synthetic results do not establish real-world model performance. All 24 local Python tests and the corresponding branch GitHub CI checks passed. Flutter and Docker builds are not validated. No application deployment is claimed.

## Why authorization did not create separate repositories

The GitHub app installation is confirmed to cover **all repositories**. The owner has admin rights. Neither fact grants the app every account-level permission. GitHub rejected repository creation and profile writes as “Resource not accessible by integration”.

A second official GitHub CLI browser authorization completed successfully. However, API response metadata in this managed workspace still identified the original connected app and reported no OAuth scopes; repository creation remained denied. The same result occurred outside the command sandbox with inherited network routing. No more authorization in this chat is needed to establish the owner's consent. The effective credential used for these API requests remains the limitation. This is distinct from an automatic approval-review rejection; no such review rejected repository creation.

## Finish automatically on your own computer

The script below uses GitHub CLI's browser login on your own computer, where this workspace's credential routing is absent. It verifies account and effective OAuth scopes before making changes, creates four public project repositories plus the special profile repository, pushes the existing project commits, updates descriptions/topics, publishes the profile README and sets the approved bio/location. It refuses to overwrite different destination histories. If interrupted, rerun it; existing matching project commits are preserved.

Requirements: official GitHub CLI (https://cli.github.com/), Git and Python 3.10+.

```bash
gh auth login --hostname github.com --web --git-protocol https --scopes repo,workflow,user
gh repo clone Abdulllah999/AI-Powered-Retention-Command-Center-Churn-Simulator
cd AI-Powered-Retention-Command-Center-Churn-Simulator
python publish_portfolio.py
```

On systems where Python 3 is named `python3`, use that command instead. Run these commands in your own terminal, not the restricted workspace. No password or token is requested by the script. The official GitHub browser handles authentication. The publisher is syntax-checked and its permission guard was verified here; its remote creation path cannot be exercised with this workspace's effective app credential.

GitHub profile pins remain a manual website action: **Customize your pins** → Interview Evidence, Market Forecast, Sentiment Baseline, Retention, Health Patterns.

Alternatively, create the five empty public repositories using https://github.com/new; with all-repository app access already enabled, the connected tools can then populate them without another authorization.
