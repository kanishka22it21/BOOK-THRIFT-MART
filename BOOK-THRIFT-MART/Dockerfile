# Use official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the application port (Flask default is 5000)
EXPOSE 5000

# Define the command to run the Flask application
CMD ["python", "main.py"]
