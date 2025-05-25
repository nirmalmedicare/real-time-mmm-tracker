# Real-Time MMM Tracker

🚀 FastAPI + MLflow microservice to train and track marketing mix models.

## Features
- `/train` logs model to MLflow
- `/predict` returns dummy predictions
- Dockerized for clean local or cloud deployment

## Usage
```bash
docker build -t mmm-tracker .
docker run -p 8000:8000 mmm-tracker
