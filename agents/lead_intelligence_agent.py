from state import add_lead

def handle(request):
    """
    Deterministic lead qualification logic.
    """

    budget = request.get("budget_range", "")
    timeline = request.get("timeline_days", 0)

    # Simple deterministic scoring
    intent_score = 1
    category = "cold"
    next_action = "follow_up"

    if budget and timeline > 0:
        intent_score = 3
        category = "warm"
        next_action = "call"

    if budget and timeline <= 30 and timeline > 0:
        intent_score = 5
        category = "hot"
        next_action = "site_visit"

    lead = {
        "lead_id": request.get("lead_id"),
        "client_name": request.get("client_name", ""),
        "source": request.get("source", "unknown"),
        "budget_range": budget,
        "timeline_days": timeline,
        "intent_score": intent_score,
        "category": category,
        "next_action": next_action,
        "next_action_due": "within 24 hours",
        "disqualification_reason": "",
        "notes": "Lead evaluated by deterministic rules"
    }

    add_lead(lead)
    return lead
