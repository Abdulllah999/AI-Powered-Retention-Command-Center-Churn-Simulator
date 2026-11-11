# Retention scenarios and SQL cohort analysis

An interactive Streamlit dashboard for exploring synthetic customer-risk scenarios, paired with a SQLite reporting exercise. The strongest evidence here is the transparent baseline comparison and reconciliation of report totals.

**Python · Streamlit · Pandas · Scikit-learn · Plotly · SQLite**

[SQL query](analytics/cohorts.sql) · [Report output](artifacts/cohort-report.csv) · [Model evaluation](artifacts/evaluation.json) · [Tests](test_app.py)

## Why a baseline matters

The 300 fictional customers receive a score from a known rule:

```text
clip(100 - engagement + 7.5 × support tickets, 0, 100), rounded to one decimal
```

| Method | Held-out MAE, synthetic score points |
| --- | ---: |
| Exact generating formula | **0.0000** |
| Random forest | 1.6647 |
| Training-mean baseline | 24.2133 |

The fixed seed-42 split contains 240 training and 60 test rows. The forest approximates a known rule, so the formula is the right solution when that rule is available. A high R² here does not establish useful churn prediction. The target is an invented score, not an observed churn event or calibrated probability.

![Interactive retention scenario dashboard](artifacts/demo.png)

## SQL question: how do the cohorts differ?

`report.py` loads the same snapshot into an in-memory SQLite database. A CTE, conditional aggregation and a window denominator produce cohort size, customer share, monthly-spend sum and the proportion with synthetic scores of at least 70.

The report reconciles to **300 customers**, a **129,937.14 snapshot spend sum** and **173 high-score rows**. These are fixture totals, not business achievements or recurring revenue. Segment labels are independently generated, so apparent cohort differences do not establish behavioral segments or causal effects.

```bash
python report.py
python -m pytest test_report.py -q
```

Tests reconcile counts, sums and threshold totals to the source, then check empty-snapshot and single-cohort denominators. [Query and interpretation](analytics/README.md).

## Run the dashboard

Python 3.12, from the repository root:

```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
. .venv/bin/activate
pip install -r requirements-dev.txt
streamlit run myfile.py --browser.gatherUsageStats=false
```

Open http://localhost:8501. Change cohort filters and scenario inputs to inspect the model approximation. The application handles empty filter selections. No credentials or external data are required.

## Inspect and validate

```bash
python -m pytest -q
python evaluate.py
```

- `retention.py`: deterministic generator, model fit and explicit baseline metrics.
- `myfile.py`: dashboard, cohort charts and scenario controls.
- `analytics/cohorts.sql` and `report.py`: reproducible reporting workflow.
- `test_app.py` and `test_report.py`: model, interface and reconciliation checks.

Feature importance does not establish causality. Moving a slider is a scenario calculation, not a measured intervention. The local app is not a deployed retention system.

## Next evidence gap

A real churn study needs a legally usable observed-outcome dataset, a defined prediction date/horizon, customer-separated chronological validation and calibration analysis. An analyst extension should add a data dictionary and a BI report on an attributed public dataset. This project uses no employer, billing or patient records.

The original source had no license; [licensing review](LICENSE-REVIEW.md) records that boundary. No license has been imposed on that original work.

## Other portfolio work

- [Sentiment classification under domain shift](https://github.com/Abdulllah999/sentiment-baseline-lab): attributed public-data benchmark, predictions and error analysis.
- [Chronological forecasting](https://github.com/Abdulllah999/market-forecast-lab): persistence baseline and sentiment ablation.
- [Resume evidence workflow](https://github.com/Abdulllah999/interview-evidence-lab): deterministic text matching for human review.
- [Synthetic model-serving API](https://github.com/Abdulllah999/health-patterns-demo): validated request contract and educational scope.

[GitHub profile](https://github.com/Abdulllah999) · [Role-specific summaries](CAREER-NOTES.md). Older `projects/` snapshots and portfolio branches are retained; the individual repositories contain current implementations.
