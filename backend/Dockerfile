# Use an official Python runtime
FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements first for dependency caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the application
COPY app /app

# Expose port
EXPOSE 8000

# Run the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
