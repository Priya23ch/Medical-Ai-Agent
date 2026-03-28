from typing import TypedDict, List, Optional

class AgentState(TypedDict):
    clinical_notes: str
    extracted_codes: Optional[dict]
    policy_status: Optional[str]
    audit_trail: List[str]