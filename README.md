# Smart Parking Management System

## Description
A production-ready parking management web app with a polished dark-mode interface, SQLite database persistence, and a simple REST API for managing vehicles.

## Features
- Park a vehicle through a modern web form
- View all parked vehicles in a dashboard-style table
- Calculate parking fees automatically
- Persist data in a SQLite database
- Show real-time totals for vehicles and collection
- Dark-mode UI for a premium experience

## Project Files
- app.py – Flask web application and UI
- parking_service.py – Database-backed parking logic
- vehicle.py – Original vehicle model classes
- tests/test_app.py – Regression tests for the service and API

## How to Run

```bash
python -m pip install flask pytest
python -m flask --app app run
```

Then open http://127.0.0.1:5000/

## Verification
The app has been verified with automated tests:

```bash
python -m pytest -q
```

