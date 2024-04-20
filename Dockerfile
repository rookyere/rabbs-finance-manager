# FROM python:3

# WORKDIR /usr/src/app

# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt
# COPY . .
# RUN python manage.py makemigrations
# RUN python manage.py migrate

# CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8000" ]


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
# CMD ["python", "./manage.py", "runserver", "0.0.0.0:8000"]
ENTRYPOINT [ "bash","-c","python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000" ]
# CMD ["python", "./manage.py", "runserver"]
