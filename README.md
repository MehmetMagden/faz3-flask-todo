# Flask Todo List — Dockerized

A simple Todo List web application built with Flask and PostgreSQL, fully containerized with Docker Compose.

## Tech Stack

- **Backend:** Python / Flask
- **Database:** PostgreSQL 15
- **Container:** Docker + Docker Compose
- **Web Server:** Flask dev server (port 5000)

## Project Structure
faz3-flask-todo/ ├── app/ │ ├── app.py # Flask application │ ├── requirements.txt # Python dependencies │ ├── Dockerfile # Flask image │ └── templates/ │ └── index.html # UI template ├── docker-compose.yml # Service orchestration ├── Makefile # Shortcuts └── README.md

## Quick Start

```bash
make build    # Build Docker image
make up       # Start all services
make down     # Stop all services
make logs     # View logs
make status   # Check container status
make clean    # Stop + remove volumes
Usage
Open browser: http://localhost:5000

Add a task → type and click Add
Complete a task → click ✅
Delete a task → click 🗑️
Services
Service	Image	Port
web	python:3.11-slim (custom)	5000
db	postgres:15-alpine	5432