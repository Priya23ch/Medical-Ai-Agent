from langgraph.graph import StateGraph, END
from .state import AgentState
from .agents import extraction_agent, validator_agent

# 1. Graph banayein
workflow = StateGraph(AgentState)

# 2. Nodes (Steps) add karein
workflow.add_node("extract", extraction_agent)
workflow.add_node("validate", validator_agent)

# 3. Connections (Edges) banayein
workflow.set_entry_point("extract")
workflow.add_edge("extract", "validate")
workflow.add_edge("validate", END)

# 4. Compile karein
app = workflow.compile()

# --- TESTING ---
if __name__ == "__main__":
    test_input = {
        "clinical_notes": "Patient has severe chest pain. Ordered EKG (CPT 93000).",
        "audit_trail": []
    }
    
    print("--- Starting Medical AI Agent ---")
    result = app.invoke(test_input)
    
    print("\nFINAL DECISION:", result["policy_status"])
    print("\nAUDIT TRAIL:")
    for step in result["audit_trail"]:
        print(f"- {step}")