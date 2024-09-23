### Todo

- [ ] Add db endpoints

# FastAPI Poetry Hello World

This is a simple Hello World API built with FastAPI and Poetry. It also features Docker, Docker Compose, and Dev Containers for easy development and deployment.

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

8. You're all set! 🎉 The API should now be running locally at `http://localhost:8000`.

## Documentation

- Access the Swagger UI documentation: [http://localhost:8000/documentation](http://localhost:8000/documentation)
- Access the ReDoc documentation: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Docker Compose

1. Build and run the Docker container using Docker Compose:

```bash
docker-compose up -d
```

2. You're all set! 🎉 The API should now be running in a Docker container at `http://localhost:8000`.

## Docker

1. Build the Docker image:

```bash
docker build -t greeting-api .
```

2. Run the Docker container:

```bash
docker run -d -p 8000:8000 greeting-api
```

3. You're all set! 🎉 The API should now be running in a Docker container at `http://localhost:8000`.

## Dev Containers

1. Open the project in Visual Studio Code.
1. Click on the Remote Explorer icon in the Activity Bar.
1. Click on the Plus icon on the DEV CONTAINERS section.
1. Select "Open Current Folder in Container" from the context menu.
1. Visual Studio Code will now build the Dev Container and open a new window in the containerized environment.

## Usage

Once the API is running, you can interact with it using your preferred API client or web browser. Here are some example requests:

- Visit `http://localhost:8000/` to see the Greeting welcome message.
- Visit `http://localhost:8000/morning` to receive a cheerful morning greeting.
- Visit `http://localhost:8000/night` to receive a soothing night-time message.

Feel free to explore and enjoy the friendliness of this API! If you have any questions or feedback, don't hesitate to reach out.

## 🤝 Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated. Star the project if you like it.

- Fork the Project
- Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
- Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
- Push to the Branch (`git push origin feature/AmazingFeature`)
- Open a Pull Request
