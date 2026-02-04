from state import get_plan

def handle(request):
    plan = get_plan()
    digest_type = request.get("digest_type")

    if plan is None:
        return {
            "digest_type": digest_type,
            "date": "03-Feb-2026",
            "notes": "No active plan found."
        }

    tasks = plan.get("tasks", [])

    if digest_type == "AM":
        return {
            "digest_type": "AM",
            "date": plan.get("date_range"),
            "top_focus": [t["title"] for t in tasks if t["priority"] == "P1"],
            "schedule_blocks": [
                f'{t["time_block"]} {t["title"]}' for t in tasks
            ],
            "notes": "Day briefing generated from active plan."
        }

    if digest_type == "PM":
        completed = [t["title"] for t in tasks if t["status"] == "done"]
        pending = [t["title"] for t in tasks if t["status"] != "done"]

        return {
            "digest_type": "PM",
            "date": plan.get("date_range"),
            "completed": completed,
            "pending": pending,
            "notes": "End-of-day wrap based on actual execution."
        }

    return None
