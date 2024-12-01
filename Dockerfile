# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask app files into the container
COPY . .

# Expose the port Flask runs on
EXPOSE 5000

# Set the command to run the Flask app
CMD ["python", "main.py"]
