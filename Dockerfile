# Use the official Python base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Install the required Python packages
RUN pip3 install flask

# Copy the entire Flask app directory to the container
COPY . .

# Expose the port that Flask is running on (replace 5000 with your Flask app's port if different)
EXPOSE 5000

# Run the Flask app using the python command (you can replace "app.py" with the name of your main Flask file)
CMD ["python", "src/app.py"]
