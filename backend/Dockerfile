# Dockerfile for Flask API

# Use Python 3.10 base image
FROM python:3.10

# Set working directory inside the container
WORKDIR /app

# Copy the dependencies file
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the Flask application code
COPY . .

# Expose the port on which Flask runs
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "backend.py"]