# Use the official Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install Flask and transformers
RUN pip install Flask transformers torch

# Make port 5000 available to the world outside this container
EXPOSE 5013

# Run the application
CMD ["python", "app.py"]