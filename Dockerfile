FROM debian:latest
MAINTAINER docker@kala.li

# ENV telegram_token=$ttoken

WORKDIR /Kala2X_Bot
RUN apt-get update
RUN apt-get install -y ffmpeg python3-pip git

RUN git clone https://github.com/Kalabint/webm2mp4.git
WORKDIR /Kala2X_Bot/webm2mp4

RUN pip3 install --user -r requirements.txt
COPY config.json ./
RUN sed -i 's/""/"${ttoken}"/g' config.json
RUN python3 bot.py
