# Using Docker with Python 3.13

- Here's how to get started using Docker with Python 3.13:

- Download this repository.

- Open the folder in your preferred editor, like Visual Studio Code.

- Start the Docker image with docker `compose up --build`.

- Create your Python files inside the _python_ folder.

## How to Run a Python File Using Attach Shell

We'll use the Docker extension in Visual Studio Code to make running Python files inside the container easier.

### Steps:

1. Ensure your container is running (`docker compose up`).
2. In VS Code, click the Docker icon on the left sidebar.
3. Find the container named `introduction-python-with-docker-app` (or whatever your container is called) in the list of running containers.
4. Right-click on the container and select **Attach Shell**.
5. A terminal will open directly inside the container.

### To test your container, run the following commands:

- python --version


### Running Python file

Now, to run a Python file, type the following in the terminal:

```
python your_file_name.py
```

Replace `your_file_name.py` with the name of the file you want to run.

> This way, you can run as many files as you want without needing to restart the container for each execution.
