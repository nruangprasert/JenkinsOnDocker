# Use an official Python runtime as a base image
FROM python:3.13-slim

# Set the working directory in the container
WORKDIR /usr/app

# Copy the application files to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask runs on
EXPOSE 5000

# Run the application
CMD ["python", "flask-monitoring-app/app.py"]
