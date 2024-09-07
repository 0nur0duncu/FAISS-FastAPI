# Base image olarak Python'un resmi imajını kullan
FROM python:3.9-slim

# Çalışma dizinini oluştur
WORKDIR /app

# Gereksinim dosyasını ve uygulama kodunu çalışma dizinine kopyala
COPY . .

# Gereksinimleri yükle
RUN pip install --no-cache-dir -r requirements.txt

# Uvicorn kullanarak FastAPI uygulamasını başlat
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000", "--reload"]

# docker build -t fast-server .
# docker run -p 5000:5000 fast-server


