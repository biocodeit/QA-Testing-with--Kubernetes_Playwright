# Use an official Playwright image that includes Python and all browser dependencies.
FROM mcr.microsoft.com/playwright/python:v1.55.0-noble

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies first.
# This step is cached, so it only re-runs if your requirements change.
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy all your test-related files from the host to the container.
# The .dockerignore file will prevent the virtual environment from being copied.
COPY . .

# Set the default command to run your tests.
# This will be the command executed when the container starts.
CMD ["pytest", "tests/test_svg.py"]
