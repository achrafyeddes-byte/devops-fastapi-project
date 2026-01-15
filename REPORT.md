# Final Project Report
**Student:** Achraf Yeddes

## Summary of Deliverables
- **Repo & Code:** Complete. FastAPI app with tests (`tests/`).
- **CI/CD:** Complete. Pipeline runs Unit Tests -> Security (SAST) -> Docker Build -> Push.
- **Docker Image:** Published to [Docker Hub](https://hub.docker.com/r/achrafyeddes/devops-todo-app).
- **Deployment:**
    - Local: Docker container runs successfully.
    - Cloud/K8s: Manifests provided in `k8s/deployment.yaml`.
- **Observability:**
    - Metrics: Implemented via `prometheus-fastapi-instrumentator`.
    - Logs: Structured JSON logs with unique `trace_id`.
- **Security:**
    - SAST: Bandit scanner runs in CI pipeline.
    - DAST: ZAP Scan performed on running container; report attached in `reports/`.