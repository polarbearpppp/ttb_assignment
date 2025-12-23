# 1. Use an official Python image (instead of Conda, we use slim Python for speed)
FROM python:3.10-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy the requirements file from your local machine to the container
COPY requirements.txt .

# 4. Install the libraries (this replaces 'conda install')
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy your code (main.py, schemas.py, etc.)
COPY . .

# 6. Run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]