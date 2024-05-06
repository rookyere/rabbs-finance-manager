# Use official Python image as the base image
FROM python:3

# Set the working directory within the container
WORKDIR /usr/src/app

# Copy requirements.txt to the working directory
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application code to the working directory
COPY . .


# Command to start the Django development server
ENTRYPOINT ["./entrypoint.sh"]
