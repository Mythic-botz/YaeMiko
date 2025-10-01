FROM python:3.11.9

# Set working directory
WORKDIR /root/Mikobot

# Copy project files
COPY . .

# Install system dependencies (ffmpeg + curl)
RUN apt-get update && apt-get install -y \
    ffmpeg \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip & setuptools
RUN pip install --upgrade pip setuptools

# Install Python dependencies
RUN pip install -U -r requirements.txt

# Run the bot
CMD ["python3", "-m", "Mikobot"]