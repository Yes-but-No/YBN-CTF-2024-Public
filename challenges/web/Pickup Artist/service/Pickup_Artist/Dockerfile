# Base image
FROM node:18

# Set working directory
WORKDIR /usr/src/app

# Copy package.json and package-lock.json if available
COPY package*.json ./

# Install node modules
RUN npm install

# Copy the application code
COPY . .

# Create the user_compliments directory
RUN mkdir -p /usr/src/app/views/user_compliments

# Change the permissions for all files and directories to be read-only, except for `views/user_compliments`
RUN find /usr/src/app -type f -exec chmod 444 {} \; \
    && find /usr/src/app -type d -exec chmod 555 {} \; \
    && chmod 777 /usr/src/app/views/user_compliments \
    && find /usr/src/app/views/user_compliments -type f -exec chmod 666 {} \;

# Use a non-root user to further restrict permissions
RUN useradd -m appuser && chown -R appuser /usr/src/app/views/user_compliments
USER appuser

# Expose the port the app runs on
EXPOSE 3000

# Start the application
CMD [ "node", "index.js" ]
