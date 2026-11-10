import json
from retention import generate_customer_data, fit_model
print(json.dumps(fit_model(generate_customer_data())[3],indent=2))
