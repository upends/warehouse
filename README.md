# Dockerized Django Application

Before you begin, ensure you have the following installed on your system:

- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/)

 
 ## Clone the Repository

Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/upends/warehouse.git
```

## Build and Run the Docker Containers

1. Open a terminal and navigate to the root directory of the cloned repository.
2. Build the Docker images using the following command:

   ```bash
   docker-compose build
   ```

3. Once the images are built successfully, start the Docker containers:

   ```bash
   docker-compose up
   ```

4. The application should now be running. You can access it at `http://localhost:8000`.
