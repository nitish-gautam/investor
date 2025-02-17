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

## 📌 Technical Overview

The solution is designed to demonstrate knowledge of the following layers of a software system:

1. **Data Layer** - Storing and managing investor and commitment data.
2. **Backend Services** - FastAPI provides REST APIs for retrieving investor and commitment data.
3. **Web Applications** - React frontend fetches data from the backend and visualizes it with filtering options.
4. **Containerization** - Docker is used for easy deployment.

## 🔧 Tech Stack Used

- **Frontend:** React (Material UI for styling, Chart.js for data visualization)
- **Backend:** Python (FastAPI)
- **Database:** SQLite (for simplicity, can be replaced with PostgreSQL or MongoDB in production)
- **API Documentation:** Swagger (`http://localhost:8000/docs`)
- **Containerization:** Docker & Docker Compose for easy setup and deployment.

### 📌 API & Frontend URLs

```
API Docs: http://localhost:8000/docs
Frontend: http://localhost:3000
```

---

## 🚀 Running the Application with Docker Compose

You can **build and run the entire application** (both backend and frontend) using **Docker Compose**.

```
docker compose up --build
```

This will:
• Build and start the backend (FastAPI) and frontend (React).
• Automatically serve the frontend via Nginx and the backend via Uvicorn.

To stop the containers:

```
docker compose down
```

## 🖥️ Running Backend Manually

If you prefer to run the backend separately:

📌 Restart Backend

To restart the backend service, stop and remove the existing container, then rebuild and run it:

```

docker stop investors_container
docker rm investors_container
docker build -t investors-app .
docker run -d -p 8000:8000 --name investors_container investors-app

```

📌 Persistent SQLite Storage

By default, the SQLite file (investors.db) is stored inside the container.
To ensure data persists between restarts, mount a volume:

```

docker run -d -p 8000:8000 \
 -v $(pwd)/backend/investors.db:/app/investors.db \
 --name investors_container investors-app

```

## 🖥️ Running Frontend Manually

If you want to start the frontend manually outside of Docker, you can run:

```
cd frontend
npm install  # Run this only the first time
npm start
```

This will start the frontend on http://localhost:3000.

📦 Project Structure

```
investor
│── backend/ # FastAPI Backend
│ ├── app/ # Backend source code
│ ├── Dockerfile # Dockerfile for backend
│ ├── requirements.txt # Backend dependencies
│── frontend/ # React Frontend
│ ├── src/ # Frontend source code
│ ├── Dockerfile # Dockerfile for frontend
│ ├── package.json # React dependencies
│── data/ # Contains data.csv
│── docker-compose.yml # Docker Compose file
│── README.md # Project documentation
│── .gitignore # Ignoring unnecessary files
```
