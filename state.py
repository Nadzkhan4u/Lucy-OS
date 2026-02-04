# Shared in-memory state (temporary)
# Later replace with DB or file persistence

CURRENT_PLAN = None

def set_plan(plan):
    global CURRENT_PLAN
    CURRENT_PLAN = plan

def get_plan():
    return CURRENT_PLAN

def update_task_status(task_id, new_status):
    if CURRENT_PLAN is None:
        return False, "No active plan"

    for task in CURRENT_PLAN.get("tasks", []):
        if task["task_id"] == task_id:
            task["status"] = new_status
            return True, f"Task {task_id} updated to {new_status}"

    return False, f"Task {task_id} not found"
