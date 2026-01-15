# we used an official Python runtime as a parent image
# and a "slim" version to keep the image small
FROM python:3.10-slim

# we set the working directory in the container
WORKDIR /app

# we copy the requirements file into the container
COPY requirements.txt .

# we install any needed packages specified in requirements.txt
# we use --no-cache-dir to keep the image smaller
RUN pip install --no-cache-dir -r requirements.txt

# we copy the rest of the application code
COPY . .

# we make port 8000 available to the world outside this container
EXPOSE 8000

# we run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]