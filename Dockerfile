# Production Dockerfile for AgriIntel on Render
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies for OpenCV and image operations
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies (using CPU PyTorch for lightweight image size)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Set environment variables
ENV PORT=10000
ENV PYTHONUNBUFFERED=1

EXPOSE 10000

# Run with Gunicorn WSGI server
CMD ["sh", "-c", "gunicorn backend.server:app --bind 0.0.0.0:${PORT:-10000} --workers 1 --threads 4 --timeout 120"]
