URL Shortener Django Project with Docker Compose
URL Shortener

Overview
URL Shortener is a simple Django web application that allows administrators to create shortened URLs for long URLs. Users can then use the shortened URLs to access the original long URLs.

Features
Shorten long URLs to generate unique shortened URLs.
Redirect users to the original long URL when they access the shortened URL.
Protect the URL shortening functionality with user authentication.
API endpoints for adding long URLs and retrieving original URLs from the shortened URL code.
API documentation with Swagger UI and OpenAPI specifications.
Docker Compose Scenario
The Docker Compose configuration for the URL shortener project defines two services:

django_app: This service runs the Django web application. It is built using the provided Dockerfile (located in the project root directory) and runs the Django development server on port 8000. The service is connected to the db service to access the PostgreSQL database.

db: This service uses the official PostgreSQL Docker image to run a PostgreSQL database. The service stores the database data in a named volume called postgres_data, ensuring data persistence between container restarts.

Both services are part of the same Docker network, enabling communication between them. The Django application depends on the db service to ensure that the database container is started before the Django container.

Installation and Setup
Follow these steps to set up the URL shortener Django project with Docker Compose:

Clone the repository:
bash
Copy code
git clone https://github.com/your_username/url-shortener-django.git
cd url-shortener-django
Build and run the Docker containers:
bash
Copy code
docker-compose up -d --build
The URL shortener application will be accessible at http://localhost:8000/.

API Endpoints
The URL shortener API provides the following endpoints:

POST /add_long_url/: Add a long URL to the URL shortener. (Admin Only)
GET /get_short_url/?short_url=<code>: Retrieve the original URL from the short URL code. (Admin Only)
API Documentation
The API documentation is available through Swagger UI. After starting the development server, visit http://localhost:8000/swagger/ to interact with the API and explore the available endpoints.

Configuration
You can customize the project settings by modifying the settings.py file. The MAIN_DOMAIN setting should be set to the main domain of your application. This domain will be used when redirecting users to the original long URLs.