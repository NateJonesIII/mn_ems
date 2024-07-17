# Dockerfile

# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT=8000

# Set working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    nodejs \
    npm \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy package.json and package-lock.json and install npm dependencies
COPY package.json package-lock.json /app/
RUN npm install

# Copy Tailwind CSS input file and config file
COPY src/styles.css /app/src/styles.css
COPY tailwind.config.js /app/tailwind.config.js

# Build Tailwind CSS
RUN npx tailwindcss -i ./src/styles.css -o ./static/css/tailwind.css

# Copy the rest of the project files into the container
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Run Django migrations
RUN python manage.py migrate

# Expose port 8000 to the outside world
EXPOSE 8000

# Command to run the application
CMD ["gunicorn","--bind","0.0.0.0:8000", "python", "manage.py", "runserver","myproject.wsgi:application"]
#"mnems-kw2es23pba-ue.a.run.app"