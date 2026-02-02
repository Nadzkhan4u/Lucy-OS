from orchestrator import route_request
from agents.finance_logging_agent import handle as finance_handle
from agents.planning_agent import handle as planning_handle
from utils.schema_validator import validate_schema

# Incoming request
request = {
    "request_id": "req-002",
    "classified_intent": "planning"
}

# Route request via orchestrator
routing = route_request(request)

if routing["agent"] is None:
    print("No agent assigned")

elif routing["agent"] == "planning_agent":
    result = planning_handle(request)

elif routing["agent"] == "finance_logging_agent":
    result = finance_handle(request)

else:
    print("Agent not implemented")
    exit()

# Validate agent output
is_valid, message = validate_schema(
    routing["schema"],
    result
)

print("Agent Output:", result)
print("Validation:", message)
