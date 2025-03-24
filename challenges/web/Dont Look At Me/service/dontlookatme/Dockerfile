# Use the official Nginx image as the base image
FROM nginx:alpine

# Copy your static files to the default Nginx public directory
COPY . /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
