# Use Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements text file 
COPY requirements.txt .

# Copy project scripts
COPY . /app


# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Create  folders to save data and the plots images 
RUN mkdir -p /app/output/data /app/output/plots


# Run project automatically
CMD ["python", "-m", "app.main"]

