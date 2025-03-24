# Use the official Node.js image as the base image
FROM node:14

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install the project dependencies
RUN npm install

# Copy the rest of the application code to the working directory
COPY . .

# Expose the port the app runs on
EXPOSE 3000
ENV FLAG=YBN24{ProTotYpE_Po1lU710N_and_eJ5?}
# Command to run the application
CMD [ "node", "index.js" ]
