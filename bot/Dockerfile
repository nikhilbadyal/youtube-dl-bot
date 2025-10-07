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

# Copy bot code
COPY . /app

# Create temp directory for downloads
RUN mkdir -p /app/temp

# Run the bot
CMD ["python", "main.py"]
