# Use a Python Alpine image as the base
FROM python:3.11-alpine

# Expose the application port
EXPOSE 1337

# Install necessary packages
RUN apk add --no-cache socat
RUN apk add --no-cache bash

# Set the working directory inside the container
WORKDIR /app/

# Copy the application files and startup script
COPY server.py .
COPY startup.sh .

# Make the startup script executable
RUN chmod +x startup.sh

# Use the startup script as the entry point
ENTRYPOINT ["./startup.sh"]
