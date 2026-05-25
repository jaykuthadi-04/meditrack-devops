# Start from an official Python image
# This is like choosing a base operating system
FROM python:3.11-slim

# Set the working directory inside the container
# All commands after this run inside /app
WORKDIR /app

# Copy requirements file first
# We do this separately for caching benefits (explained below)
COPY requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy the rest of our app code
COPY . .

# Tell Docker our app runs on port 5000
EXPOSE 5000

# Command to start our app when container runs
CMD ["python", "app.py"]