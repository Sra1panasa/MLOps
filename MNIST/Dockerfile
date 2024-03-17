# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Install Poppler, OpenCV dependencies, and other dependencies
#RUN apt-get update && apt-get install -y \
#    tesseract-ocr \
#    poppler-utils \
#    libgl1-mesa-glx \
#    && rm -rf /var/lib/apt/lists/*

# Copy only the requirements.txt file
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your project
COPY . /app

# Make port 8000 available outside this container
EXPOSE 8000

#RUN pip install openai==0.28

# Run the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000","--timeout-keep-alive", "120"]
