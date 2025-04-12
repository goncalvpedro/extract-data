FROM python:3.13-slim

RUN apt-get update && apt-get install -y \
    firefox-esr \
    wget \
    curl \
    gnupg \
    unzip \
    gcc \
    libpq-dev \
    libx11-xcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxi6 \
    libxtst6 \
    libnss3 \
    libxrandr2 \
    libasound2 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 6060

CMD ["python", "src/scraping/scraper.py"]
