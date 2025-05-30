# FROM python:3.9-slim

# WORKDIR /app
# COPY . .

# RUN pip install -r requirements.txt
# CMD ["python", "app/main.py"]
# Use Python base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy the entire repo to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port used by Flask
EXPOSE 5000

# Run the Flask app
CMD ["python", "app/main.py"]
