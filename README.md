# FastAPI Application

This is a FastAPI application that provides a REST API for handling receipts and items. The app is containerized and can be easily run using Docker.

## Prerequisites

- **Docker**: Make sure Docker is installed on your machine. You can download it from [https://www.docker.com/get-started](https://www.docker.com/get-started).
- **Python 3.12** (if running without Docker): This app is built with Python 3.12. Install it if you intend to run the app locally without Docker.


## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/rohitkotecha14/fetch-receipt-processor.git
cd fetch-receipt-processor
```

### 2. Build and Run With Docker

To run this app with Docker, follow these steps:

1. Build The docker image
   ```bash
   docker build -t receipt-collector .
   ```
2. Run the Docker Container
   ```bash
   docker run -p 8000:8000 receipt-collector
   ```
This will start the FastAPI application in a Docker container, and it will be accessible at: http://localhost:8000


## API Documentation
Once the app is running, you can access the interactive API documentation at: <br>
Swagger UI: http://localhost:8000/docs <br>
ReDoc: http://localhost:8000/redoc




