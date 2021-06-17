FROM debian:latest
MAINTAINER docker@kala.li

# Set up Prerequisites
WORKDIR /Kala2X_Bot
RUN apt-get update
RUN apt-get install -y ffmpeg python3-pip git

# Get Bot-Code from Github
RUN git clone https://github.com/Kalabint/webm2mp4.git skipcache
WORKDIR /Kala2X_Bot/webm2mp4

# Set up Bot Requirements and copy Config file
RUN pip3 install --user -r requirements.txt
COPY config.json ./

#Define ENV_Vars
ENV FFMPEG_THREADS 2
ENV TMP_PATH /tmp/
ENV TELEGRAM_TOKEN CHANGE_ME!

# Starting Bot Startup Script
COPY startup.sh ./
RUN chmod +x /Kala2X_Bot/webm2mp4/startup.sh
RUN /Kala2X_Bot/webm2mp4/startup.sh
