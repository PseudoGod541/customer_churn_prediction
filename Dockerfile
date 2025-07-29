# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set an environment variable to prevent apt-get from hanging
ENV DEBIAN_FRONTEND=noninteractive

# Update apt and install system-level dependencies and build tools
# This is crucial for compiling Python packages like numpy, scipy, etc.
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    libffi-dev \
    libssl-dev \
    libatlas-base-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy your application code into the container
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Define the command to run your application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]