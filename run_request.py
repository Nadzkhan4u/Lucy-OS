from orchestrator import route_request
from agents.planning_agent import handle as planning_handle
from agents.lead_intelligence_agent import handle as lead_handle
from agents.task_update_agent import handle as task_update_handle
from agents.daily_digest_agent import handle as digest_handle
from utils.schema_validator import validate_schema

# STEP 1 — Create today's plan
planning_handle({
    "request_id": "req-plan",
    "classified_intent": "planning"
})

# STEP 2 — New lead comes in
lead_request = {
    "request_id": "req-lead-001",
    "classified_intent": "lead",
    "lead_id": "lead-001",
    "client_name": "Ramesh",
    "source": "instagram",
    "budget_range": "30-35L",
    "timeline_days": 20
}

lead_route = route_request(lead_request)
lead_result = lead_handle(lead_request)

is_valid, message = validate_schema(
    lead_route["schema"],
    lead_result
)

print("\nQualified Lead:", lead_result)
print("Validation:", message)

# STEP 3 — AM Digest
am_request = {
    "request_id": "req-am",
    "classified_intent": "daily_digest",
    "digest_type": "AM"
}

am_route = route_request(am_request)
am_result = digest_handle(am_request)

print("\nAM Digest:", am_result)

# STEP 4 — PM Digest
pm_request = {
    "request_id": "req-pm",
    "classified_intent": "daily_digest",
    "digest_type": "PM"
}

pm_route = route_request(pm_request)
pm_result = digest_handle(pm_request)

print("\nPM Digest:", pm_result)
