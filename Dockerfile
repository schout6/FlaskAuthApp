# Use the official Python base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . .

# Set the entry point for the container
CMD ["flask", "run", "--host=0.0.0.0"]

# Expose the port used by your Flask application
EXPOSE 5000
