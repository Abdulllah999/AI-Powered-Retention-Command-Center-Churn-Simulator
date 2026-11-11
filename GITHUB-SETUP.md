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
| interview-evidence-lab | Human-reviewed skill evidence and interview prompts from fictional resume text. New portfolio implementation. | python, flask, nlp, recruitment, portfolio |
| sentiment-baseline-lab | Reproducible three-class TF-IDF baseline with authored fixtures, holdout evaluation and abstention. | python, scikit-learn, sentiment-analysis, nlp, machine-learning |
| health-patterns-demo | Educational synthetic symptom-pattern ML API and web demo with Flutter companion source. Not a diagnostic tool. | python, flask, machine-learning, synthetic-data, flutter |
| market-forecast-lab | Walk-forward forecasting with synthetic sentiment, price-only ablation and persistence baseline. | python, flask, time-series, forecasting, model-evaluation |
| AI-Powered-Retention-Command-Center-Churn-Simulator | Interactive Streamlit dashboard for synthetic customer-risk scenarios, with reproducible evaluation and explicit baselines. Educational portfolio demo. | python, streamlit, scikit-learn, plotly, data-science, synthetic-data, model-evaluation, dashboard |

Set description/topics with the gear beside **About** on each repository page. These API updates were denied; they have not been applied automatically.

## Recommended pins

On https://github.com/Abdulllah999 choose **Customize your pins**, then select `interview-evidence-lab`, `market-forecast-lab`, `sentiment-baseline-lab`, `AI-Powered-Retention-Command-Center-Churn-Simulator`, and `health-patterns-demo`.

For repository descriptions and topics, use the gear beside **About** on each repository page. These are metadata changes; all project source and profile content are already public.

## Technical validation

31 local Python tests and all five evaluation commands passed during preparation. Each individual project has its own GitHub Actions validation workflow. Synthetic/authored evaluation results do not establish real-world model performance. Flutter and Docker builds remain unvalidated; applications are not deployed.
