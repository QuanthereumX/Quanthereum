# Dockerfile - QuanthereumX Backend
# Author: Przemek Buczek

# Używamy obrazu Python 3.10 jako bazowego
FROM python:3.10

# Ustawiamy katalog roboczy w kontenerze
WORKDIR /app

# Kopiujemy pliki projektu
COPY . .

# Instalujemy zależności
RUN pip install --no-cache-dir -r requirements.txt

# Eksponujemy port 8000 dla API i WebSocketów
EXPOSE 8000

# Uruchamiamy aplikację
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
