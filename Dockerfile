# Dockerfile

# Pull base image
FROM python:3.8.3-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set working directory
RUN mkdir /app
WORKDIR /app

# Install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Add current directory to working directory
ADD . /app/
