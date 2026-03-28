import json
from .tools import check_policy

def extraction_agent(state):
    """Doctor ke note se codes extract karne ka natak (Mocking)"""
    # Maan lijiye AI ne ye extract kiya
    codes = {"cpt": "93000", "icd10": "R07.9"} 
    
    state["extracted_codes"] = codes
    state["audit_trail"].append(f"AI Extraction Success: {codes}")
    return state

def validator_agent(state):
    """Policy database check karega (Actual Logic)"""
    codes = state["extracted_codes"]
    # Ye humare tools.py se policy check karega
    result = check_policy(codes["cpt"], codes["icd10"])
    
    state["policy_status"] = result
    state["audit_trail"].append(f"Compliance Check: {result}")
    return state