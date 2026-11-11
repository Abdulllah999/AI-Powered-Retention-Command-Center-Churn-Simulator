-- Synthetic snapshot: score >= 70 is an illustrative threshold, not observed churn.
WITH cohorts AS (
    SELECT Segment AS segment,
           COUNT(*) AS customers,
           SUM(Monthly_Spend) AS monthly_spend_sum,
           AVG(Churn_Risk) AS mean_synthetic_risk,
           SUM(CASE WHEN Churn_Risk >= 70 THEN 1 ELSE 0 END) AS high_score_customers
    FROM customers
    GROUP BY Segment
)
SELECT segment, customers,
       ROUND(100.0 * customers / SUM(customers) OVER (), 2) AS customer_share_pct,
       ROUND(monthly_spend_sum, 2) AS monthly_spend_sum,
       ROUND(mean_synthetic_risk, 2) AS mean_synthetic_risk,
       high_score_customers,
       ROUND(100.0 * high_score_customers / customers, 2) AS high_score_pct
FROM cohorts
ORDER BY mean_synthetic_risk DESC, segment;
