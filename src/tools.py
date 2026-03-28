import json
import os

def check_policy(cpt: str, icd10: str):
    # JSON file load karna
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "../data/policy_db.json")
    
    with open(file_path, "r") as f:
        policies = json.load(f)
    
    if cpt in policies:
        rule = policies[cpt]
        if icd10 in rule["required_icd10"]:
            return f"APPROVED: {rule['description']} is medically necessary for {icd10}."
        else:
            return f"DENIED: {icd10} does not justify {rule['description']}."
    return "DENIED: CPT code not found in policy database."