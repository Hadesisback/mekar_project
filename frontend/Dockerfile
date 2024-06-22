# Dockerfile for Next.js app

# Use Node.js base image with LTS version
FROM node:lts-alpine

# Set working directory inside the container
WORKDIR /app

# Copy package.json and yarn.lock to install dependencies
COPY package.json .

COPY . .
# Install dependencies

RUN npm install -g pnpm 

RUN pnpm install

RUN pnpm build

# Expose the port on which Next.js runs (usually 3000 by default)
EXPOSE 5001

# Command to run Next.js in production mode
CMD ["pnpm", "start"]