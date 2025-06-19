FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y tesseract-ocr tesseract-ocr-eng \
    libglib2.0-0 libxext6 libsm6 libxrender1 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV TESSERACT_PATH=/usr/bin/tesseract

CMD ["bash", "entrypoint.sh"]
