from datetime import date, timedelta
from state import (
    get_plan,
    get_leads,
    set_weekly_plan
)

def handle(request):
    today = date.today()
    week_days = [(today + timedelta(days=i)).isoformat() for i in range(7)]

    daily_plan = get_plan()
    leads = get_leads()

    # ---- Rollover Tasks ----
    rollover_tasks = []
    if daily_plan:
        for task in daily_plan.get("tasks", []):
            if task.get("status") != "done":
                rollover_tasks.append(task["title"])

    # ---- Revenue Focus ----
    revenue_focus = []
    escalation_focus = []

    for lead in leads:
        category = lead.get("category")
        name = lead.get("client_name", "Client")
        flags = lead.get("flags", [])

        if category in ["hot", "warm"]:
            revenue_focus.append(f"{category.upper()} – {name}")

        # Escalation surfacing
        if "auto_escalated_to_hot" in flags:
            escalation_focus.append(f"ESCALATED TO HOT – {name}")

        if "stalled" in flags:
            escalation_focus.append(f"STALLED HOT LEAD – {name}")

    weekly_plan = {
        "week_start": week_days[0],
        "week_end": week_days[-1],
        "top_5_goals": [
            "Resolve escalated and stalled hot leads",
            "Close hot leads",
            "Advance warm leads",
            "Clear rollover tasks",
            "Maintain pipeline hygiene"
        ],
        "rollover_tasks": rollover_tasks,
        "revenue_focus": revenue_focus,
        "escalation_focus": escalation_focus,
        "daily_outline": {
            day: "Revenue + execution blocks"
            for day in week_days
        }
    }

    set_weekly_plan(weekly_plan)
    return weekly_plan
