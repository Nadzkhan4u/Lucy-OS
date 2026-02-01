from orchestrator import route_request
from agents.finance_logging_agent import handle
from utils.schema_validator import validate_schema

request = {
    "request_id": "req-001",
    "classified_intent": "finance"
}

routing = route_request(request)

if routing["agent"] is None:
    print("No agent assigned")
else:
    result = handle(request)

    is_valid, message = validate_schema(
        routing["schema"],
        result
    )

    print("Agent Output:", result)
    print("Validation:", message)
# agents/finance_logging_agent.py