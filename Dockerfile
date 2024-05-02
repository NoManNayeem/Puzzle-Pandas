# Use the latest Python 3.12 image
FROM python:3.12.0-slim

# Prevent Python from writing pyc files to disc (optional)
ENV PYTHONDONTWRITEBYTECODE 1
# Prevent Python from buffering stdout and stderr (optional)
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends gcc

# Copy the project requirements file
COPY requirements.txt /app/

# Install project dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the project files to the container
COPY . /app/

# Run gunicorn server on container start
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "PuzzlePanda.wsgi:application"]
