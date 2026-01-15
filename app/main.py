import time
import uuid
import logging
from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List, Optional
from prometheus_fastapi_instrumentator import Instrumentator

# --- 1. Setup Structured Logging ---
# We force the logs to be in simple JSON format
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger("devops-logger")

# --- 2. Data Models ---
class Task(BaseModel):
    id: Optional[int] = None
    title: str
    is_completed: bool = False

# --- 3. Initialize App ---
app = FastAPI(title="Simple DevOps ToDo API")

# --- 4. Setup Prometheus Metrics ---
# This automatically creates the /metrics endpoint
Instrumentator().instrument(app).expose(app)

# --- 5. Middleware for Logs & Tracing ---
@app.middleware("http")
async def log_requests(request: Request, call_next):
    # Generate a unique Trace ID for this request
    trace_id = str(uuid.uuid4())
    start_time = time.time()
    
    # Process the request
    response = await call_next(request)
    
    # Calculate duration
    process_time = time.time() - start_time
    
    # Create the structured log entry (JSON)
    log_entry = {
        "trace_id": trace_id,
        "method": request.method,
        "path": request.url.path,
        "status_code": response.status_code,
        "duration": round(process_time, 4)
    }
    
    # Print as a stringified dictionary (effectively JSON)
    logger.info(str(log_entry))
    
    # Add trace ID to response headers (useful for debugging)
    response.headers["X-Trace-ID"] = trace_id
    return response

# --- 6. Application Logic ---
fake_task_db: List[Task] = []
task_counter = 1

@app.get("/")
async def root():
    return {"status": "ok", "message": "Service is healthy"}

@app.get("/tasks", response_model=List[Task])
async def get_tasks():
    return fake_task_db

@app.post("/tasks", response_model=Task, status_code=201)
async def create_task(task: Task):
    global task_counter
    task.id = task_counter
    fake_task_db.append(task)
    task_counter += 1
    return task