# Use the Python 3.13 image.
FROM python:3.13

# Set the working directory in the container.
WORKDIR /app

# Install the Python dependencies.
RUN pip install requests

# Copy all your Python files into the container.
COPY . /app