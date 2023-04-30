# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Set the environment variable
ENV NAME World

# Run the command to start the app
CMD ["python", "fun_facts.py"]
