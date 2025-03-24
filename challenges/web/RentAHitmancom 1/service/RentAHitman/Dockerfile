# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV SECRET_KEY="$(python -c 'import secrets; print(secrets.token_hex(32))')"
ENV FLAG1="YBN24{I7_W4SN't_R3@lly_sQl1_WAS_1T?}"
ENV FLAG2="YBN24{WHO_PuT_cRYpTO_IN_MY_w3B_chAlL?}"

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN mkdir -p /app/databases && chmod -R 777 /app/databases

# Install any necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install additional dependencies for encryption
RUN apt-get update && apt-get install -y \
    libssl-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Expose port 5000 for Flask
EXPOSE 5000

# Set the Flask environment variables
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the command to start the Flask server
CMD ["flask", "run"]
