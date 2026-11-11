import pytest
from retention import generate_customer_data
from report import cohort_report

def test_cohorts_reconcile_to_source():
    data = generate_customer_data()
    report = cohort_report(data)
    assert report.customers.sum() == len(data)
    assert report.monthly_spend_sum.sum() == pytest.approx(data.Monthly_Spend.sum())
    assert report.high_score_customers.sum() == (data.Churn_Risk >= 70).sum()
    assert report.customer_share_pct.sum() == pytest.approx(100, abs=.02)

def test_empty_snapshot():
    assert cohort_report(generate_customer_data().iloc[:0]).empty

def test_single_cohort_denominator():
    data = generate_customer_data()
    data['Segment'] = 'One cohort'
    report = cohort_report(data)
    assert len(report) == 1
    assert report.customer_share_pct.iloc[0] == 100
    assert report.high_score_pct.iloc[0] == pytest.approx(
        100 * (data.Churn_Risk >= 70).mean(), abs=.0051)
