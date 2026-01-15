# DevOps FastAPI Project

![CI/CD](https://github.com/achrafyeddes-byte/devops-fastapi-project/actions/workflows/ci-cd.yaml/badge.svg)
![Docker](https://img.shields.io/badge/docker-containerized-blue)

**Student:** Achraf Yeddes
**Deliverables Status:**  All Technical Requirements Met

## Project Overview
A containerized ToDo API demonstrating a complete DevOps lifecycle:
1.  **CI/CD:** Automated testing and security scanning via GitHub Actions.
2.  **Docker:** Fully containerized application available on Docker Hub (`achrafyeddes/devops-todo-app`).
3.  **Kubernetes:** Deployment and Service manifests included in `k8s/` folder.
4.  **Observability:** Prometheus metrics (`/metrics`), JSON logging, and Tracing.
5.  **Security:** SAST (Bandit) and DAST (OWASP ZAP) implemented.

## How to Run
```bash
# Run with Docker
docker run -p 8000:8000 achrafyeddes/devops-todo-app:latest

