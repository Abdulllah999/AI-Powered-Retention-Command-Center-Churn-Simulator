# Portfolio publication and profile settings

All five new repositories now exist and have been populated: the special profile repository `Abdulllah999` and the four project repositories listed below. The owner created the empty repositories; the connected integration transferred the existing project commits and published the profile README. No further repository creation or login is needed for the prepared portfolio.

## Remaining account settings

GitHub denied API writes to profile settings and repository descriptions/topics with HTTP 403 “Resource not accessible by integration”. These settings have not been applied. Set them through the GitHub website if desired.

At https://github.com/settings/profile use:

- Name: Abdullah Shakeel
- Location: Islamabad, Pakistan
- Bio: Data science & AI | Python, SQL & ML | Building reproducible models and useful data applications | Islamabad, Pakistan

No LinkedIn, website or public email is added without a verified intended professional link.

## Repository metadata

| Repository | Description | Topics |
| --- | --- | --- |
| interview-evidence-lab | Deterministic resume skill evidence and interview prompts for human review, with Flask validation tests. | python, flask, nlp, recruitment, portfolio |
| sentiment-baseline-lab | Cross-domain sentiment benchmark on attributed UCI reviews, with source holdout, reproducible predictions and error analysis. | python, scikit-learn, sentiment-analysis, nlp, machine-learning |
| health-patterns-demo | Educational synthetic symptom-pattern ML API and web demo with Flutter companion source. Not a diagnostic tool. | python, flask, machine-learning, synthetic-data, flutter |
| market-forecast-lab | Walk-forward forecasting with synthetic sentiment, price-only ablation and persistence baseline. | python, flask, time-series, forecasting, model-evaluation |
| AI-Powered-Retention-Command-Center-Churn-Simulator | Interactive Streamlit dashboard for synthetic customer-risk scenarios, with reproducible evaluation and explicit baselines. Educational portfolio demo. | python, streamlit, scikit-learn, plotly, data-science, synthetic-data, model-evaluation, dashboard |

Set description/topics with the gear beside **About** on each repository page. These API updates were denied; they have not been applied automatically.

## Recommended pins

On https://github.com/Abdulllah999 choose **Customize your pins**, lead with `sentiment-baseline-lab`, `market-forecast-lab` and `AI-Powered-Retention-Command-Center-Churn-Simulator`. Add `interview-evidence-lab` and `health-patterns-demo` as supporting Python/API projects.

For repository descriptions and topics, use the gear beside **About** on each repository page. These are metadata changes; all project source and profile content are already public.

## Technical validation

31 local Python tests and all five evaluation commands passed during preparation. Each individual project has its own GitHub Actions validation workflow. Sentiment now includes a separate public UCI binary benchmark; the other evaluation fixtures remain synthetic/authored. Each result must be described with its dataset and protocol. Flutter and Docker builds remain unvalidated; applications are not deployed.
