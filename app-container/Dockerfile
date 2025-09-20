# Stage 1: Build the static website
# We don't need a build stage for a static site, so we can go straight to the server.
# This is a good practice for more complex sites with build tools like Webpack.

# Stage 2: Serve the website with Nginx
FROM nginx:alpine

# Copy the static website files into the Nginx public directory
COPY . /usr/share/nginx/html

# Expose port 80 to the outside world
EXPOSE 80

# The Nginx server starts automatically, so no need for a CMD instruction.