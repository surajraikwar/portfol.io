# We Use an official Python runtime as a parent image
FROM python:3.6

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /portfolio

# Set the working directory
WORKDIR /portfolio

# install psycopg2 dependencies
RUN apt-get update
RUN apt-get install -y postgresql postgresql-contrib gcc python3-dev musl-dev

# Copy the current directory contents into the container at /portfol_io
ADD . /portfolio

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8000
CMD exec gunicorn portfol_io.wsgi:application — bind 0.0.0.0:8000 — workers 3

