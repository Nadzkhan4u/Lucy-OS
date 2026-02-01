from utils.schema_validator import validate_schema

sample_data = {
    "transaction_id": "txn-001",
    "type": "expense",
    "timestamp": "02-Feb-2026 14:30 IST",
    "amount": 350,
    "currency": "INR",
    "category": "Travel",
    "mode": "UPI",
    "note": "Cab ride",
    "verified": True
}

is_valid, message = validate_schema(
    "schemas/finance_log.schema.json",
    sample_data
)

print(message)
