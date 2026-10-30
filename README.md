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