# Use a lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files (only what's needed)
COPY etl/ etl/
COPY config/ config/
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set entry point (modify based on your main ETL script)
CMD ["python", "etl/main.py"]
