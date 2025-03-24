# Use the official Python image as a base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1  
ENV PYTHONUNBUFFERED=1         

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

ENV FLASK_APP=main.py
ENV SECRET_KEY='p+u2Mvm>JWD:k{bj]F_BY}'
ENV FLAG='YBN24{8@ba_!S_A_B@d_PRo6rAmm3R}'
# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Expose the port the app runs on
EXPOSE 5000

# Define the command to run the app
CMD ["flask", "run", "--host=0.0.0.0"]
