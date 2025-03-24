# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Install wget, gnupg, curl, and other necessary packages
RUN apt-get update && apt-get install -y wget gnupg2 apt-transport-https curl unzip

# Add Google Chrome's signing key
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

RUN apt install -y chromium chromium-driver

# Set display port as an environment variable
ENV DISPLAY=:99
ENV ADMIN_CREDS="lBcEXKFpQVivikx5vxGmCjpUsk3ROc7SCfd35LB00i4KXOctVAVC28sgagXpRlXf"
ENV FLAG="YBN24{pHp_Is_sO_fUN_I'm_S0rRy}"
ENV WEBSITE_URL="https://sleep-is-for-the-weak-website-chall.ybn.sg"

# Set environment variable for ChromeDriver
ENV PATH /usr/local/bin:$PATH

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port (if your application requires it)
EXPOSE 12345

ENV FLASK_APP=main.py
ENV FLASK_ENV=development
# Run the AdminBot service
CMD ["flask", "run", "--host=0.0.0.0", "--port=12345"]