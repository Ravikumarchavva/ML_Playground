# Use the official Python 3.10 image
FROM python:3.10

# Set the working directory in the container
WORKDIR /fastApi

# Copy the application files
COPY ./docker ./docker
COPY ./main.py .  
# Ensure main.py is correctly copied

# Copy the requirements file
COPY ./dockerRequirements.txt ./dockerRequirements.txt

# Install the dependencies
RUN pip install --no-cache-dir -r dockerRequirements.txt

# Expose the application port
EXPOSE 8000

# Specify the c ommand to run on container start
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
