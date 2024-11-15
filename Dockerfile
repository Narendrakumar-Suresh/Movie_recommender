# Use the official slim Python image from DockerHub
FROM python:3.12-slim

# Install build dependencies and libraries required for some Python packages
RUN apt-get update && apt-get install -y \
    build-essential \
    libatlas-base-dev \
    libfreetype6-dev \
    libpng-dev \
    libopenblas-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt to the container
COPY requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project to the container
COPY . /app

# Expose the port that Streamlit will run on
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "main.py"]
