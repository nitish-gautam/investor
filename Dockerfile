# Use a lightweight Python base image
FROM python:3.10-slim

# Make a directory in the container
WORKDIR /app

# Copy your backend code
COPY ./backend /app/backend

# Copy the data folder with data.csv
COPY ./data /app/data

# Switch to the backend folder so pip sees requirements.txt
WORKDIR /app/backend

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Initialize the DB by running init_db.py
RUN python init_db.py

# Expose port 8000
EXPOSE 8000

# By default, start the FastAPI server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
