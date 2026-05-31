FROM mcr.microsoft.com/playwright/python:v1.44.0-jammy

WORKDIR /app

# Prevent Python from writing .pyc files and force unbuffered logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV HEADLESS=True

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your test suite
COPY . .

# Run pytest by default
CMD ["pytest", "-v", "-s"]