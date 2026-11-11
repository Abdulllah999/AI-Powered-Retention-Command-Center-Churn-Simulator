# SQL cohort analysis

Run from the repository root after installing requirements:

```bash
python report.py
python -m pytest test_report.py -q
```

The existing seeded generator supplies 300 fictional customer snapshots. Pandas loads them into an in-memory SQLite database; `cohorts.sql` uses a CTE, conditional aggregation and a window denominator to report cohort size, share, summed monthly spend and synthetic score distribution. No credentials or configuration are required. SQLite is included with Python.

The question is: how do cohort composition and invented risk scores vary in this snapshot? A score of 70 is an illustrative reporting threshold. Spend is an input snapshot sum, not measured recurring revenue; segment labels are generated independently and do not establish meaningful customer behavior. No churn rate, retention effect, time trend or causal result can be inferred.

Tests reconcile totals to the source and check empty and single-cohort denominators. For a real analyst case study, replace this fixture only with appropriately licensed public data, define business measures with a data dictionary, and add time-based analysis and a BI report. No employer or patient data belongs here.

## Measured example output

[CSV produced by `python report.py`](../artifacts/cohort-report.csv) contains four cohorts and 300 synthetic customers. The snapshot monthly-spend sum is 129,937.14; 173 rows have an invented score of at least 70. These are fixture totals, not business achievements.
