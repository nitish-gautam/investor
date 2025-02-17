# ----------------------------------------
# Frontend Dockerfile for React + Nginx
# ----------------------------------------

# ------------------------------
# Stage 1: Build the React App
# ------------------------------
FROM node:18-alpine AS builder

# Set working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json (if available) to leverage Docker caching
# This ensures that dependencies are not re-installed unless package.json changes
COPY frontend/package*.json ./

# Install dependencies
# Using --legacy-peer-deps to avoid dependency conflicts in some setups
RUN npm install --legacy-peer-deps

# Copy the rest of the frontend project files to the container
COPY frontend ./

# Build the React application for production (minified, optimized)
RUN npm run build

# ----------------------------------------------
# Stage 2: Serve the React App using Nginx
# ----------------------------------------------
FROM nginx:alpine

# Copy the built frontend files from the previous stage (builder)
COPY --from=builder /app/build /usr/share/nginx/html

# Expose port 3000 for the React frontend
EXPOSE 3000

# Start Nginx to serve the frontend application
CMD ["nginx", "-g", "daemon off;"]
