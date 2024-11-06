#Use the official Python 3.12 image as base
FROM python:3.12-slim

#Set the working directory
WORKDIR /app

#Copy requirements.txt file to the container
COPY requirements.txt .

#Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

#Copy the rest of the application code to the container
COPY . .

#Expose the port for FastAPI
EXPOSE 8000

#Command for running FastAPI using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]