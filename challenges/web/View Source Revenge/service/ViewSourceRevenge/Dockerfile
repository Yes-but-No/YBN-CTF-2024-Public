# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file into the container
COPY requirements.txt ./

# Install any necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Replace the specific line in Werkzeug as root
RUN sed -i 's/elif self._failed_pin_auth.value > 10:/elif False:/' /usr/local/lib/python3.11/site-packages/werkzeug/debug/__init__.py
RUN sed -i 's/self.trusted_hosts: list\[str\] = \[".localhost", "127.0.0.1"\]/self.trusted_hosts: list[str] = [".localhost", "127.0.0.1", "view-source-revenge-viewsourcerevenge-chall.ybn.sg"]/' /usr/local/lib/python3.11/site-packages/werkzeug/debug/__init__.py

# Create a new user and group with a secure name
RUN useradd -m very_secure_username

# Change ownership of the working directory to the newly created user
RUN chown -R very_secure_username:very_secure_username /usr/src/app

# Switch to the new user
USER very_secure_username

# Copy the application code into the container
COPY . /usr/src/app
RUN mv /usr/src/app/Dockerfile.clean /usr/src/app/Dockerfile
# Set environment variables
ENV FLASK_APP=main.py
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["flask", "run", "--host=0.0.0.0"]
