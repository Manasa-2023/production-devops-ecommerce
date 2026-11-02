# Production DevOps E-Commerce Platform

## Project Overview

This project demonstrates how to build, test, containerize,
deploy, secure, and monitor a web application using DevOps practices.

## Technology Stack

- Backend: Python and FastAPI
- Frontend: React (planned)
- Database: PostgreSQL
- Version Control: Git and GitHub
- CI/CD: GitHub Actions
- Containers: Docker
- Infrastructure as Code: Terraform
- Cloud: AWS (planned)
- Orchestration: Kubernetes (planned)
- Monitoring: Metrics, logs, and alerts (planned)

## Project Goals

- Automate application testing and deployment.
- Build reproducible container images.
- Manage infrastructure using code.
- Apply security and reliability practices.
- Monitor application health and troubleshoot failures.
- Document implementation decisions and lessons learned.

## Progress

- [x] Prepare Python, Git, and VS Code
- [ ] Initialize the project repository
- [ ] Build the application
- [ ] Create the CI/CD pipeline
- [ ] Deploy and monitor the application

## Automated Testing

The application uses pytest and FastAPI TestClient
to verify API behavior.

### Tests implemented

- Health endpoint returns HTTP 200.
- Health endpoint returns the expected JSON response.
- Home endpoint returns HTTP 200.
- Home endpoint returns the expected project information.

### Run tests

```powershell
python -m pytest -v

## Docker Containerization

### Objective

Package the FastAPI application and its runtime dependencies into a Docker image to support consistent execution across development, testing, and deployment environments.

### Implementation

- Created a Dockerfile using Python 3.12 slim as the base image.
- Installed application dependencies from `requirements.txt`.
- Configured Uvicorn to listen on `0.0.0.0:8000` inside the container.
- Built the image `ecommerce-api:1.0`.
- Started a container named `ecommerce-api`.
- Published container port 8000 on host port 8000.
- Added `.dockerignore` to exclude unnecessary files from the build context.

### Commands used

```powershell
docker build -t ecommerce-api:1.0 .
docker run -d --name ecommerce-api -p 8000:8000 ecommerce-api:1.0
docker ps
docker logs ecommerce-api
Invoke-RestMethod http://localhost:8000/health
```

### Verification

- Docker image built successfully.
- Container started successfully.
- Container port mapping was verified.
- Health endpoint returned `{"status":"healthy"}`.

### DevOps value

Containerization provides a repeatable application package, simplifies environment setup, and establishes a foundation for automated image builds and cloud deployments.

### Current limitations

This is a learning implementation. Production hardening, automated container testing, image versioning, vulnerability scanning, non-root execution, and deployment automation will be addressed in later project stages.