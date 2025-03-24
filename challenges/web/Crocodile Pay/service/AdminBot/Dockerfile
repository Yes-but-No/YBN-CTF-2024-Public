# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Install wget, gnupg, curl, and other necessary packages
RUN apt-get update && apt-get install -y wget gnupg2 apt-transport-https curl unzip

# Add Google Chrome's signing key
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

# Set up the Chrome repository
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

# Install Google Chrome
RUN apt-get update && apt-get install -y google-chrome-stable --fix-missing

# # Download the matching ChromeDriver version
RUN wget -O /tmp/chromedriver.zip https://storage.googleapis.com/chrome-for-testing-public/131.0.6778.69/linux64/chromedriver-linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver-linux64/chromedriver -d /usr/local/bin/ && \
    mv /usr/local/bin/chromedriver-linux64/chromedriver /usr/local/bin/chromedriver && \
    rm -rf /usr/local/bin/chromedriver-linux64 && \
    rm /tmp/chromedriver.zip

# Set display port as an environment variable
ENV DISPLAY=:99

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
