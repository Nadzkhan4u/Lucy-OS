from state import update_task_status

def handle(request):
    task_id = request.get("task_id")
    new_status = request.get("new_status")

    success, message = update_task_status(task_id, new_status)

    return {
        "task_id": task_id,
        "new_status": new_status,
        "success": success,
        "message": message
    }
