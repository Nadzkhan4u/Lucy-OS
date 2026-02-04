from datetime import date
from state import get_leads, set_weekly_plan, _write_json, _read_json
import os

LEADS_FILE = os.path.join("data", "leads.json")

def handle(request):
    today = date.today()
    leads = get_leads()

    escalations = []

    for lead in leads:
        created = lead.get("created_date")
        last_updated = lead.get("last_updated_date", created)

        if not created:
            continue

        age_days = (today - date.fromisoformat(created)).days

        # Warm → Hot
        if lead["category"] == "warm" and age_days >= 3:
            lead["category"] = "hot"
            lead["flags"].append("auto_escalated_to_hot")
            lead["last_updated_date"] = today.isoformat()
            escalations.append(f'{lead["client_name"]} escalated to HOT')

        # Hot → Stalled
        elif lead["category"] == "hot" and age_days >= 2:
            if "stalled" not in lead["flags"]:
                lead["flags"].append("stalled")
                escalations.append(f'{lead["client_name"]} flagged as STALLED')

        # Cold → Inactive
        elif lead["category"] == "cold" and age_days >= 7:
            lead["category"] = "inactive"
            lead["flags"].append("auto_inactive")
            escalations.append(f'{lead["client_name"]} marked INACTIVE')

    # Persist updated leads
    _write_json(LEADS_FILE, leads)

    return {
        "checked_date": today.isoformat(),
        "escalations": escalations,
        "total_leads": len(leads)
    }
