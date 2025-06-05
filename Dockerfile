# Base Image
FROM python:3.12-slim-buster

# Environment Variables

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    FLASK_APP=run.py \
    FLASK_ENV=production \
    FLASJ_RUN_PORT=5000

# Working Directory

WORKDIR /app

# Install System Dependencies

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# Install Python Dependencies

RUN pip install --upgrade pip && pip install -r requirements.txt 

# Copy The Entire Project

COPY . .

# Create Database On First Run

RUN mkdir -p /app/instance

# Expose Port (Flask Default)

EXPOSE 5000

# Start The FLask App

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]