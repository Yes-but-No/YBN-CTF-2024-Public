# Use Node.js as the base image
FROM node:18

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install --force

# Copy the rest of the application code and the .env file
COPY . .

# Expose the port Next.js runs on
EXPOSE 3000

# Set the environment variable for production
ENV NODE_ENV=production

# Start the application with Prisma initialization at runtime
CMD ["sh", "-c", "npx prisma generate && npx prisma db push && npx prisma db seed && npx prisma migrate deploy && npm run build && npm start"]
