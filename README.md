# Flask Todo List — CI/CD Pipeline

A Todo List web application with full CI/CD pipeline using GitHub Actions.

## Tech Stack

- **Backend:** Python / Flask
- **Database:** PostgreSQL 15
- **Container:** Docker + Docker Compose
- **CI/CD:** GitHub Actions
- **Testing:** pytest

## CI/CD Pipeline

Every push to master triggers:

1. **Test job** — runs pytest (4 tests)
2. **Docker job** — builds image and pushes to Docker Hub (only if tests pass)

## Project Structure
faz3-flask-todo/ ├── .github/ │ └── workflows/ │ ├── hello.yml # Hello World workflow │ ├── ci.yml # Test automation │ └── docker.yml # Docker build & push ├── app/ │ ├── app.py │ ├── requirements.txt │ ├── Dockerfile │ └── templates/ │ └── index.html ├── tests/ │ ├── init.py │ └── test_app.py ├── docker-compose.yml ├── Makefile └── README.md

## Quick Start

```bash
make build    # Build Docker image
make up       # Start all services
make down     # Stop all services
make logs     # View logs
Usage
Open browser: http://localhost:5000

Docker Hub
Image: wowmaker/flask-todo:latest

bash 
docker pull wowmaker/flask-todo:latest