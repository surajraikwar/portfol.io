# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Ensures that the python output is set straight to the terminal without buffering it first
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /portfolio

# Copy the current directory contents into the container
COPY . /portfolio

# Install psycopg2 dependencies
RUN apt-get update \
    && apt-get install -y gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8000

# Start the application
CMD ["gunicorn", "portfol_io.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
