def handle(request):
    return {
        "transaction_id": "txn-demo-001",
        "type": "expense",
        "timestamp": "02-Feb-2026 18:00 IST",
        "amount": 500,
        "currency": "INR",
        "category": "Travel",
        "mode": "UPI",
        "note": "Demo transaction",
        "verified": True
    }
# agents/finance_logging_agent.py