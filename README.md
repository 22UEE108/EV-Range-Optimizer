# EV Range Optimizer ⚡

A FastAPI-based EV range estimation and charging recommendation system that predicts whether an electric vehicle can safely complete a journey based on battery state, distance, and changing driving conditions.

## Overview

Navigation systems can provide routes and charging station locations, but they do not consider whether the vehicle has enough battery charge to safely reach those stations.

This project adds an energy feasibility layer by combining:

- Current battery SOC (State of Charge)
- Battery discharge profile
- Travel distance
- Driving conditions

The system estimates expected arrival SOC and recommends charging when the battery level is unsafe.

---
## Tech Stack

### Backend
- Python
- FastAPI (REST API development)
- Uvicorn (ASGI server)
- Pydantic (data validation)

### Data / Model
- JSON-based battery discharge profile
- MATLAB-generated SOC curve (used as battery model input)

### Development Concepts
- API-based architecture
- Data validation
- Modular backend design
- Dynamic recalculation logic

## Features

- SOC-based battery range prediction
- Battery discharge profile integration
- Traffic-aware energy consumption adjustment
- Pre-trip range estimation
- Dynamic trip condition updates
- Charging requirement alerts

---

## Project Architecture

The project follows a modular backend architecture where each component has a separate responsibility.

### 1. API Layer (FastAPI)

Handles communication between the user/vehicle system and backend.

Responsibilities:
- Receives trip information
- Validates input data using Pydantic models
- Returns prediction results

Files:
- `main.py`
- `models.py`

---

### 2. Battery Prediction Layer

Contains the EV energy estimation logic.

Responsibilities:
- Loads battery discharge profile
- Applies driving condition factors
- Estimates expected arrival SOC
- Determines charging requirement

File:
- `battery.py`

---

### 3. Battery Model Data

Stores the SOC discharge curve generated from battery modeling.

Format:

File:
- `vehicle_battery_profile.json`

---

### 4. Dynamic Update Layer

Simulates vehicle telemetry updates during a trip.

Responsibilities:
- Sends updated SOC
- Sends remaining distance
- Sends changing traffic conditions
- Triggers recalculation

File:
- `simulate_trip.py`

---



