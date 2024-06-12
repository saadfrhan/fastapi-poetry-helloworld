# Greeting API

Welcome to the Greeting API! This is a simple FastAPI (with Poetry) project that offers a friendly greeting message. The API has three endpoints: a homepage greeting, a morning greeting, and a night-time message.

## Description

This API offers three endpoints:

1. `/`: A Greeting welcome message to greet you when you visit the homepage.
2. `/morning`: A cheerful morning greeting to start your day with positivity.
3. `/night`: A soothing night-time message to wish you sweet dreams.

## Features

This project supports the following features:

- **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
- **Poetry**: A dependency management and packaging tool that helps you declare, manage, and install dependencies of Python projects.
- **Pytest**: A testing framework that makes it easy to write simple tests to validate the correctness of your code.
- **Swagger UI**: An interactive API documentation that helps you design, build, document, and consume your RESTful APIs.
- **ReDoc**: An OpenAPI/Swagger-generated API Reference Documentation that makes your API documentation more interactive and user-friendly.
- **Docker**: A platform for developing, shipping, and running applications in containers that allows you to package your application with all of its dependencies into a standardized unit for software development.
- **Dev Containers**: A feature of Visual Studio Code that allows you to develop your project in a container-based environment, ensuring that you have all the necessary tools and dependencies to work on the project.

## Installation

To install and run this API locally, follow these steps:

1. Clone this repository to your local machine:

```bash
git clone https://github.com/saadfrhan/fastapi-poetry-helloworld
```

2. Navigate to the project directory:

```bash
cd fastapi-poetry-helloworld
```

3. Install the dependencies using poetry:

```bash
poetry install
```

4. Activate Poetry virtual environment:

```bash
poetry shell
```

5. Adjust active python interpreter from your code editor settings (if needed). Set that Python interpreter as active which shows the virtual environment name in between.

6. Run test files:

```bash
poetry run pytest -v
```

7. Run the FastAPI server:

```bash
poetry run start
```

8. You're all set! 🎉 The API should now be running locally at `http://127.0.0.1:8000`.

## Documentation

- Access the Swagger UI documentation: [http://127.0.0.1:8000/documentation](http://127.0.0.1:8000/documentation)
- Access the ReDoc documentation: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Docker

1. Build the Docker image:

```bash
docker build -t greeting-api .
```

2. Run the Docker container:

```bash
docker run -d -p 8000:8000 greeting-api
```

3. You're all set! 🎉 The API should now be running in a Docker container at `http://

## Dev Containers

1. Open the project in Visual Studio Code.
1. Click on the Remote Explorer icon in the Activity Bar.
1. Click on the Plus icon on the DEV CONTAINERS section.
1. Select "Open Current Folder in Container" from the context menu.
1. Visual Studio Code will now build the Dev Container and open a new window in the containerized environment.

## Usage

Once the API is running, you can interact with it using your preferred API client or web browser. Here are some example requests:

- Visit `http://127.0.0.1:8000/` to see the Greeting welcome message.
- Visit `http://127.0.0.1:8000/morning` to receive a cheerful morning greeting.
- Visit `http://127.0.0.1:8000/night` to receive a soothing night-time message.

Feel free to explore and enjoy the friendliness of this API! If you have any questions or feedback, don't hesitate to reach out.

## 🤝 Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated. Star the project if you like it.

- Fork the Project
- Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
- Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
- Push to the Branch (`git push origin feature/AmazingFeature`)
- Open a Pull Request
