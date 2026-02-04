from state import set_plan, get_leads

def handle(request):
    leads = get_leads()

    tasks = [
        {
            "task_id": "t-001",
            "title": "Daily admin & review",
            "time_block": "09:30–10:00 IST",
            "priority": "P2",
            "dependency": "",
            "buffer_minutes": 5,
            "expected_outcome": "Inbox and task review",
            "status": "planned"
        }
    ]

    task_counter = 2
    time_slots = {
        "call": "10:00–11:00 IST",
        "site_visit": "12:00–14:00 IST"
    }

    for lead in leads:
        if lead["category"] == "hot":
            tasks.append({
                "task_id": f"t-{task_counter:03}",
                "title": f"Site visit – {lead.get('client_name','Client')}",
                "time_block": time_slots["site_visit"],
                "priority": "P1",
                "dependency": "",
                "buffer_minutes": 30,
                "expected_outcome": "Advance hot lead toward closure",
                "status": "planned"
            })
            task_counter += 1

        elif lead["category"] == "warm":
            tasks.append({
                "task_id": f"t-{task_counter:03}",
                "title": f"Call – {lead.get('client_name','Client')}",
                "time_block": time_slots["call"],
                "priority": "P1",
                "dependency": "",
                "buffer_minutes": 10,
                "expected_outcome": "Qualify warm lead",
                "status": "planned"
            })
            task_counter += 1

    plan = {
        "plan_id": "plan-auto-001",
        "plan_type": "daily",
        "date_range": "03-Feb-2026",
        "owner": "Nadeem Ahmed",
        "tasks": tasks,
        "assumptions": [
            "Sales tasks auto-generated from lead intelligence",
            "Time blocks are fixed for demo purposes"
        ]
    }

    set_plan(plan)
    return plan
