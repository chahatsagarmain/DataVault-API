# DataVault API

DataVault API is a Django Rest Framework project designed for learning purposes. It provides functionality for users to store and manage files on the backend. The API supports CRUD operations, authentication, and authorization using JWT tokens.

## Features

- User management: Create, read, update, and delete user information.
- Authentication: Token-based authentication using JWT tokens.
- File storage: Upload, retrieve, and delete files associated with user accounts.

## Getting Started

### Prerequisites

- Python 3.x
- Django
- Django Rest Framework

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/DataVault-API.git
   cd DataVault-API
2. Install dependencies:
   pip install -r requirements.txt

3. Apply Migrations
   python manage.py migrate

4. Run the development server:
   python manage.py runserver

### Usage

    Create a user account using the /api/user/ endpoint (If you have the access_token).
    Else, Register your account /api/register/
    Obtain JWT tokens by making a POST request to the /token/ endpoint with valid credentials.
    Or Login and get the token at /api/login/
    Use the obtained tokens for authentication in subsequent requests. Pass it from request headers as Authorization : Bearer {access_token}
    Upload files using the /api/file/ endpoint.
    Retrieve file names associated with a user using the /file/<user_id>/ endpoint.
    Delete files using the /file/ endpoint with the file name in the request header or body as a multipart form data encrytption type.


### Api Endpoints
    API Endpoints

    /user/: User management (GET, POST)
    /user/<id>/: Get, update, or delete a user by ID (GET, PUT, DELETE)
    /user/<username>/: Update a user by username (PUT)
    /token/: Obtain JWT tokens (POST)
    /token/refresh/: Refresh JWT tokens (POST)
    /token/verify/: Verify JWT tokens (POST)
    /login/: Login user (POST)
    /register/: Register user (POST)
    /file/: File management (POST, GET, DELETE)
    /file/<user_id>/: Get file names associated with a user (GET)
    /file/: Delete a file by name (DELETE)

### Contributing

  Feel free to contribute to this project by opening issues or creating pull requests.
