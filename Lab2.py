from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

task_db = [
    {"task_id": 1, "task_title": "Laboratory Activity", "task_desc": "Create Lab Act 2", "is_finished": False}
]

class Task(BaseModel):
    task_title: str
    task_desc: str
    is_finished: bool = False

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in task_db:
        if task["task_id"] == task_id:
            return {"status": "ok", "result": task}
    raise HTTPException(status_code=404, detail={"error": "Task is not Herez"})

@app.post("/tasks")
def create_task(task: Task):
    new_task_id = len(task_db) + 1
    new_task = {"task_id": new_task_id, "task_title": task.task_title, "task_desc": task.task_desc, "is_finished": task.is_finished}
    task_db.append(new_task)
    return {"status": "ok", "result": new_task}

@app.patch("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    for task in task_db:
        if task["task_id"] == task_id:
            task["task_title"] = updated_task.task_title
            task["task_desc"] = updated_task.task_desc
            task["is_finished"] = updated_task.is_finished
            return {"status": "ok", "result": task}
    raise HTTPException(status_code=404, detail={"error": "Task is not Herez"})

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in task_db:
        if task["task_id"] == task_id:
            task_db.remove(task)
            return {"status": "ok", "result": f"Task {task_id} deleted"}
    raise HTTPException(status_code=404, detail={"error": "Task is not Herez"})