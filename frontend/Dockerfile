# Dockerfile for Next.js app

# Use Node.js base image with LTS version
FROM node:lts-alpine

# Set working directory inside the container
WORKDIR /app

# Copy package.json and yarn.lock to install dependencies
COPY package.json .

# Install dependencies
RUN npm install  # or npm install if using npm

# Copy the entire Next.js app
COPY . .

# Expose the port on which Next.js runs (usually 3000 by default)
EXPOSE 3000

# Command to run Next.js in production mode
CMD ["npm", "start"]