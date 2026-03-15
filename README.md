# Distributed Log Monitoring System

A simple system that collects application logs, stores them in a database, and analyzes them to detect errors and warnings.

## Technologies Used
- Python
- Flask
- SQLite

## Features
- Log ingestion using REST API
- Centralized log storage
- Automatic log analysis
- Error and warning detection

## API Endpoints

### Add Log
POST /add_log

Example JSON:
{
 "service":"auth_service",
 "level":"ERROR",
 "message":"database connection failed"
}

### View Logs
GET /logs

### Analyze Logs
GET /analyze

## How to Run

Install dependencies

pip install flask

Run server

python app.py

Server will start at

http://127.0.0.1:5000
