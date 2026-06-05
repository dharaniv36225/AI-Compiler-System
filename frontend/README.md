# AI App Compiler

## Objective
Natural Language → Structured Config → Validation → Runtime Preview

## Architecture

Prompt
↓
Intent Extraction
↓
Architecture Planner
↓
Schema Generator
↓
Validation Engine
↓
Repair Engine
↓
Runtime Preview

## Features

- Multi-stage pipeline
- Deterministic generation
- Validation engine
- Repair engine
- Runtime simulation
- Evaluation framework
- JSON export
- Architecture visualization

## Tech Stack

Frontend:
- React
- Vite
- Axios

Backend:
- FastAPI
- Python

## Evaluation Results

Success Rate: 85%
Failure Rate: 0%
Average Latency: 7ms

## Run Locally

Backend:
uvicorn app:app --reload

Frontend:
npm run dev