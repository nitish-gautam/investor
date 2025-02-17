# -------------------------
# Backend Dockerfile
# -------------------------

# Use a lightweight Python base image to minimize image size
FROM python:3.10-slim

# Set the working directory inside the container
# All commands will be executed inside this directory
WORKDIR /app

# Copy only the requirements file first to leverage Docker caching
# This ensures that dependencies are not re-installed unless requirements.txt changes
COPY backend/requirements.txt /app/

# Install dependencies with no-cache to keep the image lightweight
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the backend application files after installing dependencies
# This prevents unnecessary reinstallation of dependencies when only the application code changes
COPY backend /app/backend

# Copy the data folder containing initial dataset (e.g., data.csv)
COPY data /app/data

# Change the working directory to backend where the FastAPI app is located
WORKDIR /app/backend

# Expose port 8000 to allow access to the FastAPI application
EXPOSE 8000

# Define the default command to run FastAPI application with Uvicorn
# `--host 0.0.0.0` makes it accessible to other containers
# `--port 8000` binds it to the specified port
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
