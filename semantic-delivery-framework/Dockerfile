# Use Miniconda base image with Python 3.11
FROM continuumio/miniconda3

WORKDIR /app

# Copy environment file and install dependencies
COPY webapp.yml .
RUN conda env create -f webapp.yml

# Install curl (Debian-based image)
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Make conda environment the default for RUN commands
SHELL ["conda", "run", "-n", "semantic-delivery-framework", "/bin/bash", "-c"]

# Copy app source code (make sure to exclude .ipynb_checkpoints in .dockerignore)
COPY . .

# Copy wait-for-db script and make it executable
COPY wait-for-db.sh /wait-for-db.sh
RUN chmod +x /wait-for-db.sh

# Expose Flask port
EXPOSE 5000

# Run the wait-for-db script, then start Flask app
CMD ["/wait-for-db.sh", "conda", "run", "--no-capture-output", "-n", "semantic-delivery-framework", "flask", "run", "--host=0.0.0.0"]
