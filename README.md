# Smart Parking Management System

## Overview
A beginner-friendly Python project for managing a parking lot. It includes both a command-line interface and a Flask-based web application for parking, searching, removing, and tracking vehicles.

## Main OOP Concepts Used
This project is a great example of Object-Oriented Programming in Python. The main OOP concepts used are:

- Classes and Objects: The project uses classes such as Vehicle, Car, Bike, and ParkingLot.
- Inheritance: Car and Bike inherit features from the base Vehicle class.
- Encapsulation: The parking fee is protected inside the class using private attributes and methods.
- Polymorphism: The calculate_fee() method behaves differently for Car and Bike.
- Abstraction: The user interacts with simple methods like park_vehicle(), search_vehicle(), and display() without worrying about internal implementation details.

## Features
- Park vehicles through a simple CLI menu or a web form
- Store vehicle details such as vehicle number, owner name, and vehicle type
- Automatically calculate parking fees for cars and bikes
- Search for parked vehicles by vehicle number
- Remove vehicles from the parking system
- View the total parking collection
- Persist data using SQLite
- Demonstrate OOP principles in a practical project

## Project Structure
- app.py – Flask web application with HTML UI and REST API
- main.py – Command-line interface for parking operations
- parking.py – Parking lot class and core vehicle management logic
- parking_service.py – Database service layer for SQLite operations
- vehicle.py – Base Vehicle class with Car and Bike subclasses
- requirements.txt – Python dependencies

## Installation
Install the required dependencies:

```bash
python -m pip install -r requirements.txt
```

## Usage

### Web Application
Run the Flask app:

```bash
python app.py
```

Open the browser at:

```text
http://127.0.0.1:5000/
```

### Command-Line Application
Run the CLI version:

```bash
python main.py
```

## API Endpoints
The Flask app provides the following routes:
- GET /api/vehicles – Get all parked vehicles
- POST /api/vehicles – Park a new vehicle
- GET /api/vehicles/<vehicle_no> – Search a vehicle
- DELETE /api/vehicles/<vehicle_no> – Remove a vehicle

## Database
The project uses SQLite and creates a database file named:

```text
parking.db
```



