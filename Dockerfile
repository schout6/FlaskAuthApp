# Use the official Python base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN apt-get update && apt-get install -y unixodbc-dev
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . .

# Expose the port used by your Flask application
EXPOSE 5000

# Define the command to run your Flask application
CMD [ "python", "authenticator.py" ]
