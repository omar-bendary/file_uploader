# Use the official Python image from the Docker Hub
FROM python:3.10

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file into the container
COPY requirements.txt /code/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /code/

# Run migrations and start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
