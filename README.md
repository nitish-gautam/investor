# investor

FastAPI and React application that showcase list of investors and the total of their commitments.

## The User Story

The aim is to fulfill the following user story:

```
As a user,
I want to see a list of investors and the total of their commitments.
When I select an investor,
I want to see a breakdown of their commitments
And be able to filter them by Asset Class.
```

Sample data is provided in `data.csv`. Assume a sole currency of GBP, and ignore any authentication needs.

## Technical Overview

The solution is designed to demonstrate knowledge of the following layers of a software system:

Data Layer - Storing and managing investor and commitment data.
Backend Services - FastAPI provides REST APIs for retrieving investor and commitment data.
Web Applications - React frontend fetches data from the backend and visualizes it with filtering options.

## Tech Stack Used

Frontend: React (Material UI for styling, Chart.js for data visualization)
Backend: Python (FastAPI)
Database: SQLite (for simplicity, can be replaced with PostgreSQL or MongoDB in production)
API Documentation: Swagger (http://localhost:8000/docs)
Containerization: Docker for deployment

```
API Docs: http://localhost:8000/docs
Frontend: http://localhost:3000
```

## Restart Backend

To restart the backend service, stop and remove the existing container, then rebuild and run it:

```
docker stop investors_container
docker rm investors_container
docker build -t investors-app .
docker run -d -p 8000:8000 --name investors_container investors-app
```

## Persistent SQLite Storage

By default, the SQLite file (investors.db) is stored inside the container. To ensure data persists between restarts, mount a volume:

```
docker run -d -p 8000:8000 \
  -v $(pwd)/backend/investors.db:/app/investors.db \
  --name investors_container investors-app
```

## Restart Frontend

To restart the React frontend, simply run:

```
npm start
```
