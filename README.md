# Dockerized Django Application To Manage Inventory

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

## APIs

### 1. Create Product
- **Endpoint**: `POST /v1/api/product/create`
- **Description**: This API creates a new product with the provided details.
- **Request Method**: `POST`
- **Request Body**:
  ```json
  {
      "name": "Product P4",
      "category": "Clothing",
      "price": 5543.12
  }

## APIs

### 2. Get Product by ID

- **Endpoint**: `GET /v1/api/product/update/{id}`
- **Description**: This API retrieves a specific product by its ID.
- **Request Method**: `GET`
- **URL Parameters**:
  - `{id}`: The unique identifier of the product.
- **Response**:
  ```json
  {
      "name": "Product P2",
      "category": "Clothing",
      "price": 543.12
  }

### 3. Get All Products API

- **Endpoint**: `GET /v1/api/products`
- **Description**: This API retrieves all products.
- **Request Method**: `GET`
- **Response**:
  ```json
  [
      {
        "name": "Product P2",
        "category": "Clothing",
        "price": 543.12
    },
      {
        "name": "Product P4",
        "category": "Clothing",
        "price": 5543.12
    }
  ]

### 4. Update Product API

- **Endpoint**: `PATCH /api/product/update/{id}`
- **Description**: This API updates a specific product by its ID.
- **Request Method**: `PATCH`
- **URL Parameters**:
  - `{id}`: The unique identifier of the product.
- **Request Body**:
  ```json
  {
      "name": "Product P5",
      "price": 999.99
  }


### 8. Delete Product API

- **Endpoint**: `DELETE /v1/api/product/delete/{id}`
- **Description**: This API deletes a specific product by its ID.
- **Request Method**: `DELETE`
- **URL Parameters**:
  - `{id}`: The unique identifier of the product to be deleted.
