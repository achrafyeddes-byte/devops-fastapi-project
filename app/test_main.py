from fastapi.testclient import TestClient
from app.main import app

# Create a test client to make requests to our app
client = TestClient(app)

def test_read_root():
    """Test the root health check endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "message": "Service is healthy"}

def test_create_and_get_task():
    """Test creating a task and then retrieving list of tasks."""
    # 1. Create a task
    task_data = {"title": "Learn DevOps", "is_completed": False}
    response_create = client.post("/tasks", json=task_data)
    assert response_create.status_code == 201
    data = response_create.json()
    assert data["title"] == "Learn DevOps"
    assert "id" in data
    task_id = data["id"]

    # 2. Get tasks and verify the new task is there
    response_get = client.get("/tasks")
    assert response_get.status_code == 200
    tasks_list = response_get.json()
    # Ensure we found the task we just created
    found = any(task["id"] == task_id for task in tasks_list)
    assert found