# Select a existing image from https://hub.docker.com/ to build your image on top of it
FROM python:3.7-alpine
# Maintainer of that IMAGE
LABEL key="London App Developer Ltd" 

# Python needs to run inside in that doccer in unbuffered mode ( @todo study )
ENV PYTHONUNBUFFERED 1

# Copy project requirement.txt inside docker image at /requirement.txt
COPY ./requirements.txt /requirements.txt
# Install all the items listed in requirement.txt
RUN pip install -r /requirements.txt

# Make an directory to store the code
RUN mkdir /app
# Make it as a default directory so that if we run anything on docker it will run from this location
WORKDIR /app
# Copy the app code from our project to docker image
COPY ./app /app

# Ceate a user which will run our app using docker if we will not do that the app will be run by root user which is not recommended
RUN adduser -D user
USER user
