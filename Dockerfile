# Use the official Python base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /code/

# Expose the port the app runs on
EXPOSE 5000

# Run the application
CMD ["python3", "src/server.py"]
