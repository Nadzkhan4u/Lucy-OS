import json
import os

DATA_DIR = "data"
PLAN_FILE = os.path.join(DATA_DIR, "plan.json")
LEADS_FILE = os.path.join(DATA_DIR, "leads.json")

# ---------- Utility ----------

def _read_json(path, default):
    if not os.path.exists(path):
        return default
    with open(path, "r") as f:
        return json.load(f)

def _write_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

# ---------- Plan Persistence ----------

def set_plan(plan):
    _write_json(PLAN_FILE, plan)

def get_plan():
    return _read_json(PLAN_FILE, {})

# ---------- Task Updates ----------

def update_task_status(task_id, new_status):
    plan = get_plan()
    if not plan:
        return False, "No active plan"

    for task in plan.get("tasks", []):
        if task["task_id"] == task_id:
            task["status"] = new_status
            set_plan(plan)
            return True, f"Task {task_id} updated to {new_status}"

    return False, f"Task {task_id} not found"

# ---------- Lead Persistence ----------

def add_lead(lead):
    leads = _read_json(LEADS_FILE, [])
    leads.append(lead)
    _write_json(LEADS_FILE, leads)

def get_leads():
    return _read_json(LEADS_FILE, [])
