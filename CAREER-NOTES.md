# Application positioning and truthful project summaries

## Tailor applications

| Role | Lead projects | Truthful emphasis and next evidence gap |
| --- | --- | --- |
| Data Scientist | Market Forecast, Sentiment, Retention | Explain evaluation design and baseline failures. Lead with the attributed UCI cross-domain sentiment benchmark and its full error analysis; the forecast and retention results remain synthetic. |
| ML Engineer | Sentiment, Health API | Emphasize train/inference consistency, validation and CI definitions. Next add artifact versioning, integration tests and a measured serving benchmark. |
| AI Engineer | Interview Evidence, Sentiment | Emphasize bounded text workflows, abstention and human review. These projects do not establish LLM/RAG production experience. |
| Python Developer | Interview Evidence, Market Forecast | Emphasize Flask, modular code, validation and tests. Add persistence and authentication only when a real use case requires them. |
| Data Analyst | Retention | Emphasize dashboard design and the SQLite cohort report (CTE, conditional aggregation, window denominator and reconciliation tests). Both use synthetic scenarios. A licensed public dataset and a Power BI/Tableau artifact remain the clearest next evidence gap. |

## Ready-to-use project summaries

- **Interview Evidence Lab:** Built a Flask prototype that extracts explicit skill evidence from fictional resumes and job descriptions and generates consistent interview prompts, with input validation and tests.
- **Sentiment Baseline Lab:** Built a three-class TF-IDF and logistic-regression text demo with train-only preprocessing, baseline evaluation and unknown-vocabulary abstention. Added a separate binary UCI benchmark: 1,977 Amazon/Yelp training sentences and 995 held-out IMDb sentences; macro F1 0.7022 and accuracy 70.95%, versus 49.95% majority accuracy. The three-class web interface remains an authored fixture, not live Twitter data.
- **Market Forecast Lab:** Implemented expanding-window next-close forecasting with a sentiment ablation and persistence baseline on synthetic market data; reported that persistence achieved lower held-out MAE.
- **Health Pattern Explorer:** Built an educational model-serving API and web demo using synthetic symptom patterns, plus Flutter companion source that still requires mobile validation. It is not a diagnostic system.
- **Retention Simulator:** Improved a Streamlit synthetic risk dashboard with reproducible model logic, explicit baseline comparisons, empty-filter validation and a reconciled SQL cohort report.

Use “new portfolio implementation, 2026” in applications where dates or provenance could otherwise be mistaken for university project history. Do not replace the original CV project descriptions with features or technologies that were not implemented. Do not claim employment impact from these demos.

## Recruiter-facing emphasis after review

Lead with the public-data sentiment benchmark, then forecasting methodology and the SQL/dashboard work. Treat the interview evidence and health API as supporting Python exercises. None of these establishes production LLM/RAG engineering, clinical deployment or real trading performance. These remain skills/evidence gaps rather than claims to add to a CV.

Suggested sentiment summary: “Implemented a reproducible cross-domain sentiment benchmark on UCI review data, training on Amazon/Yelp and evaluating on 995 deduplicated IMDb sentences. Reported macro F1 0.7022, published all held-out errors, and added CI checks for artifact reproduction.”
