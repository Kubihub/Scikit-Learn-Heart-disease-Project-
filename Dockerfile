# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the scikit-learn script and dataset into the container
COPY scikit_learn_project.py /app
COPY heart_disease.csv /app

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir scikit-learn pandas

# Make port 80 available to the world outside this container
EXPOSE 80

# Run the scikit-learn script when the container launches
CMD ["python", "scikit_learn_project.py"]
