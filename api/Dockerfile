FROM python:3.11-slim

# Install system dependencies needed for video processing
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install additional dependencies for the API
RUN pip install --no-cache-dir fastapi uvicorn python-multipart

# Copy API code
COPY . /app

# Create files directory for downloads
RUN mkdir -p /app/files

# Expose port
EXPOSE 8000

# Run the API
CMD ["python", "main.py"]
