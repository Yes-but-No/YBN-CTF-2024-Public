# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /app
# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 5000


# Set the environment variables to specify the Flask app and environment
ENV FLASK_APP=main.py
ENV FLASK_ENV=development
# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]
