# Start your image with a node base image
FROM ubuntu:latest

# The /app directory should act as the main application directory
WORKDIR /app

# Copy the app package and package-lock.json file
COPY package*.jso	n ./

# Copy local directories to the current local directory of our docker image (/app)
COPY ./src ./src
COPY ./public ./public

# Install node packages, install serve, build the app, and remove dependencies at the end
RUN npm install \
    && npm install -g serve \
    && npm run build \
    && rm -fr node_modules
RUN apt-get install -y python-pip python-dev build-essential
RUN pip install -r requirements.txt

EXPOSE 3000

# Start the app using serve command
CMD ['backend.py']
