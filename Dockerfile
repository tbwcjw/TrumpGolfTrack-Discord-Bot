FROM python:3.10-slim

RUN apt update && apt install -y \
    wget \
    libx11-dev \
    libxcomposite-dev \
    libxrandr-dev \
    libgl1-mesa-glx \
    libnss3 \
    libgdk-pixbuf2.0-0 \
    fonts-liberation \
    libappindicator3-1 \
    libasound2 \
    xdg-utils \
    && apt clean

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb || apt install -f -y
