# Portfolio audit — 11 November 2026

## Verified account state at review

Authenticated GitHub account: `Abdulllah999`. One public repository existed at review: this retention simulator. The account bio read “Data Analyst | Python, SQL & Excel | Turning raw data into actionable business insights”; location and website were empty. This repository had a description and no topics. No special `Abdulllah999` profile repository existed.

The four portfolio branches contain new implementations, documentation, tests, screenshots, data/provenance notes and evaluation output. They are not recovered university code. The owner selected these existing implementations for continued use. No separate CV document was provided in this session; biographical details come from the pasted request. No LinkedIn or personal website was verified, so neither is invented.

## Priorities

1. Create the special profile repository and four empty project repositories, then transfer the existing branch histories. The connected GitHub integration can read/write existing source, but repository creation returned HTTP 403 “Resource not accessible by integration” in this session. Owner authorization alone does not change that API permission.
2. Publish the prepared profile README after its project targets exist. See PROFILE-README-DRAFT.md and GITHUB-SETUP.md for exact bio, location, metadata and pins. Do not publish broken featured links.
3. Keep evaluation limitations beside results. The stock persistence baseline beats both fitted models; sentiment's nine authored holdout examples are only a smoke evaluation; health results recover a synthetic generator; recruitment is deterministic keyword evidence, without personality or emotion inference.
4. Add visible SQL evidence within the existing retention project. The new `analytics/cohorts.sql` and `report.py` supply a reproducible snapshot report with reconciliation tests. A public-data BI case study remains a useful next step; more toy repositories are not a priority.

## Revalidation in this session

Python 3.12 virtual environment, pinned direct dependencies from the repositories:

| Source | Local pytest result |
| --- | --- |
| Retention, SQL report and existing publisher tests | 10 passed |
| Interview Evidence Lab | 5 passed |
| Sentiment Baseline Lab | 4 passed |
| Health Pattern Explorer | 6 passed |
| Market Forecast Lab | 6 passed |

All five evaluation commands also completed. Forecast MAE: Ridge 0.917654, price-only 0.886939, persistence 0.735564 over 71 chronological origins. Retention MAE: forest 1.66465, mean baseline 24.21335, exact formula 0. These are synthetic demonstrations. Health accuracy: 0.78 on 150 artificial cases. Sentiment accuracy: 1.0 on nine authored examples, with a 0.3333 majority baseline; this is not Twitter performance.

Previously published main and all four portfolio branches have successful GitHub Actions runs verified via the API. The README's outdated “CI has not run” sentence was corrected. Existing screenshots were inspected as repository artifacts; no fresh browser screenshot, deployment, Docker build or Flutter build is claimed in this audit. New commits require their own CI result.

## Career positioning

See CAREER-NOTES.md for role-specific emphasis and application-ready summaries. Lead with evaluation for Data Scientist, serving/validation for ML Engineer, bounded text workflows for AI Engineer, Flask/module design for Python Developer, and dashboard/SQL reconciliation for Data Analyst. Employment and education details remain owner-reported; no CV achievement is treated as independently verified.

## Default-branch publication follow-through

All four labs are now copied from their preserved `portfolio/<name>` branch commits into `projects/<name>` on the default branch. The repository front page links directly to runnable source, screenshots and evaluations. Each application retains its provenance, dependency and licensing notes. Local pytest configuration isolates the applications, and the central GitHub Actions matrix runs each project from its own directory.

All 31 Python tests and five evaluation commands passed again from the consolidated layout. Local Markdown link targets were checked with no missing paths. Repository creation, repository description/topics and profile bio/location updates were attempted again; each returned HTTP 403 “Resource not accessible by integration”. No settings update or separate repository creation is claimed. The five destination repositories did not exist at this check. Existing history and branches remain intact.

## Final publication status

The owner created all five empty public destinations. The connected integration published the profile README in `Abdulllah999` and transferred each original lab commit to the matching repository's `main` branch without rewriting history. Profile project links and screenshots now target those repositories. The portfolio overview and download/setup guides have been updated to remove pending-creation instructions. Profile bio/location, repository descriptions/topics and pins remain website actions because the integration lacks those API capabilities. Project source, documentation, screenshots, tests and evaluation artifacts are public; no deployment is claimed.
