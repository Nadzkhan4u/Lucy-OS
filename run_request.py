from orchestrator import route_request
from agents.planning_agent import handle as planning_handle
from agents.task_update_agent import handle as task_update_handle
from agents.daily_digest_agent import handle as digest_handle
from utils.schema_validator import validate_schema

# STEP 1 — Generate plan
plan_request = {
    "request_id": "req-plan",
    "classified_intent": "planning"
}
planning_handle(plan_request)

# STEP 2 — AM Digest
am_request = {
    "request_id": "req-am",
    "classified_intent": "daily_digest",
    "digest_type": "AM"
}
am_route = route_request(am_request)
am_result = digest_handle(am_request)

print("\nAM Digest:", am_result)

# STEP 3 — Mark task t-001 as done
update_request = {
    "request_id": "req-update",
    "classified_intent": "task_update",
    "task_id": "t-001",
    "new_status": "done"
}
update_route = route_request(update_request)
update_result = task_update_handle(update_request)

print("\nTask Update:", update_result)

# STEP 4 — PM Digest
pm_request = {
    "request_id": "req-pm",
    "classified_intent": "daily_digest",
    "digest_type": "PM"
}
pm_route = route_request(pm_request)
pm_result = digest_handle(pm_request)

print("\nPM Digest:", pm_result)
