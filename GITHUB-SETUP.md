**Updated:** CLI authorization was granted, but effective API requests remain restricted in this workspace. See [complete downloads and automatic local publication](COMPLETE-PROJECT-DOWNLOADS.md) for the current resolution.

# Finish the GitHub profile setup

The connected integration can push code and manage pull requests, but GitHub denied repository creation, repository descriptions/topics and profile settings with HTTP 403 / “Resource not accessible by integration”. No account permission was changed.

## Create five empty public repositories

Use https://github.com/new under owner **Abdulllah999**. Leave README, .gitignore and license initialization unchecked. Create:

1. `interview-evidence-lab`
2. `sentiment-baseline-lab`
3. `health-patterns-demo`
4. `market-forecast-lab`
5. `Abdulllah999`

If the ChatGPT GitHub app is configured for selected repositories, grant it access to these new repositories in https://github.com/settings/installations. No passwords or tokens belong in chat. Return to the conversation after creation; the source is already pushed to the `portfolio/<project-name>` branches and can be moved to the corresponding main branches without generating fake history.

The `Abdulllah999` repository is special: its root README.md becomes the account's profile front page. PROFILE-README-DRAFT.md contains the prepared content for that repository, including target links that will work after the four project repositories exist. Until then, PORTFOLIO.md is the working overview with branch links.

## Profile settings

At https://github.com/settings/profile set:

- Name: Abdullah Shakeel
- Location: Islamabad, Pakistan
- Bio: Data science & AI | Python, SQL & ML | Building reproducible models and useful data applications | Islamabad, Pakistan

Leave website, LinkedIn and public email blank unless you choose to supply verified links or an address.

## Repository metadata

| Repository | Description | Topics |
| --- | --- | --- |
| interview-evidence-lab | Human-reviewed skill evidence and interview prompts from fictional resume text. New portfolio implementation. | python, flask, nlp, recruitment, portfolio |
| sentiment-baseline-lab | Reproducible three-class TF-IDF baseline with authored fixtures, holdout evaluation and abstention. | python, scikit-learn, sentiment-analysis, nlp, machine-learning |
| health-patterns-demo | Educational synthetic symptom-pattern ML API and web demo with Flutter companion source. Not a diagnostic tool. | python, flask, machine-learning, synthetic-data, flutter |
| market-forecast-lab | Walk-forward forecasting with synthetic sentiment, price-only ablation and persistence baseline. | python, flask, time-series, forecasting, model-evaluation |
| AI-Powered-Retention-Command-Center-Churn-Simulator | Interactive Streamlit dashboard for synthetic customer-risk scenarios, with reproducible evaluation and explicit baselines. Educational portfolio demo. | python, streamlit, scikit-learn, plotly, data-science, synthetic-data, model-evaluation, dashboard |

Set description/topics with the gear beside **About** on each repository page. These API updates were denied; they have not been applied automatically.

## Pins

On https://github.com/Abdulllah999 select **Customize your pins**. After the new repositories are populated, choose Interview Evidence, Market Forecast, Sentiment Baseline, Retention, then Health Patterns. Keep the main profile centered on Python/data science/AI; do not pad repository count with unfinished projects.

## Validation status

Local Python checks: 24 passing tests. All five Python web interfaces were rendered in Chromium at desktop and mobile widths. Flutter companion and Docker recipes are not validated builds. Authored/synthetic data results are not real-world model-performance claims. Check each branch's Actions workflow for the latest remote result.
