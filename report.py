"""Run a reproducible SQLite cohort report on the existing synthetic snapshot."""
from pathlib import Path
import sqlite3
import pandas as pd
from retention import generate_customer_data

QUERY = Path(__file__).parent / 'analytics' / 'cohorts.sql'

def cohort_report(data=None):
    if data is None:
        data = generate_customer_data()
    with sqlite3.connect(':memory:') as connection:
        data.to_sql('customers', connection, index=False)
        return pd.read_sql_query(QUERY.read_text(encoding='utf-8'), connection)

if __name__ == '__main__':
    print(cohort_report().to_csv(index=False), end='')
