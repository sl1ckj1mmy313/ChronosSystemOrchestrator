# Stage 1: Build dependencies
FROM python:3.11-slim as builder

# Prevent Python from writing .pyc files and buffer stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy the requirements file and install build dependencies
COPY requirements.txt .
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    libssl-dev \
    && pip install --upgrade pip && \
    pip install --prefix=/install -r requirements.txt && \
    rm -rf /var/lib/apt/lists/*

# Stage 2: Create the final image
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copy installed dependencies from the builder stage into the final image.
COPY --from=builder /install /usr/local

# Copy the application code and configuration (including the .env file, if needed).
COPY .env /app/.env

# Expose the port on which the orchestrator will run
EXPOSE 8000

# Command to run the FastAPI application using Uvicorn.
# Adjust the module path if your FastAPI instance is named differently.
CMD ["uvicorn", "src/api/system_api:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
