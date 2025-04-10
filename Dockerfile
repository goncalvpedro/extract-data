FROM python:3.12-slim

# System dependencies
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

# Set workdir
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY . .

# Expose a port (if applicable)
EXPOSE 6060

# Run the script
CMD ["python", "src/scraping/scraper.py"]
