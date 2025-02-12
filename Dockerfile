# 1️⃣ Select the base Python image (preferably 3.9 or 3.11)
FROM python:3.9

# 2️⃣ Set the working directory
WORKDIR /quanthereum

# 3️⃣ Copy project files into the container
COPY . /quanthereum

# 4️⃣ Install required dependencies from "requirements.txt"
RUN pip install --no-cache-dir -r requirements.txt

# 5️⃣ Expose port 8000 for API / WebSocket
EXPOSE 8000

# 6️⃣ Default command to run the application
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
