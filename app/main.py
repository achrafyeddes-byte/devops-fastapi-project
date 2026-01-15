from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Define the data model for a Task using Pydantic
class Task(BaseModel):
    id: Optional[int] = None
    title: str
    is_completed: bool = False

# Initialize the FastAPI app
app = FastAPI(title="Simple DevOps ToDo API")

# In-memory storage for tasks (replacing a database for simplicity)
fake_task_db: List[Task] = []
task_counter = 1

@app.get("/")
async def root():
    """Health check endpoint."""
    return {"status": "ok", "message": "Service is healthy"}

@app.get("/tasks", response_model=List[Task])
async def get_tasks():
    """Retrieve all tasks."""
    return fake_task_db

@app.post("/tasks", response_model=Task, status_code=201)
async def create_task(task: Task):
    """Create a new task."""
    global task_counter
    # Assign an ID and add to database
    task.id = task_counter
    fake_task_db.append(task)
    task_counter += 1
    return task

# Note: We are currently well under 150 lines of code. 
# We have plenty of room left for observability later.