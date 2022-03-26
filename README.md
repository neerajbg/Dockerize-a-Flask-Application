# How to Dockerize a simple Flask Application

# Prerequisites
Install Docker Engine if not yet done. For installation please refer to official Docker - https://docs.docker.com/engine/install/

After cloning the repository run the command to build image and then run the docker container

# Build the image
docker build -t flask-app .

# Check the image 
docker images

# Run the container from the image
docker run --name flask_container -p 5000:5000 -it --rm flask-app

# Check container
docker ps

Once container is running navigate to http://127.0.0.1:5000/ in the browser.
