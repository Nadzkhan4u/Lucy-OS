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

    rollover_tasks = []
    if daily_plan:
        for task in daily_plan.get("tasks", []):
            if task.get("status") != "done":
                rollover_tasks.append(task["title"])

    revenue_focus = []
    for lead in leads:
        if lead["category"] in ["hot", "warm"]:
            revenue_focus.append(
                f'{lead["category"].upper()} – {lead.get("client_name","Client")}'
            )

    weekly_plan = {
        "week_start": week_days[0],
        "week_end": week_days[-1],
        "top_5_goals": [
            "Close hot leads",
            "Advance warm leads",
            "Complete carried-forward tasks",
            "Maintain daily follow-ups",
            "Review pipeline health"
        ],
        "rollover_tasks": rollover_tasks,
        "revenue_focus": revenue_focus,
        "daily_outline": {
            day: "Revenue + execution blocks"
            for day in week_days
        }
    }

    set_weekly_plan(weekly_plan)
    return weekly_plan
