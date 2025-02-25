# Using a lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app #inside the container

# Copy project files (only what's needed)
COPY etl/	/app/etl/
COPY tests/	/app/tests/
COPY config/	/app/config/
COPY data/	/app/data/
COPY dags/	/app/dags/
COPY require.txt .

# Install dependencies
RUN pip install --upgrade pip
RUN apt-get update && apt-get install -y \
    libpq-dev gcc build-essential python3-dev \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --no-binary psycopg2 psycopg2
RUN pip install --no-cache -r require.txt

# Set to run DAG Script
CMD ["python", "/app/dags/aviation-analysis-run.py"]

