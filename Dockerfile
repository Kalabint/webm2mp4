FROM debian:latest
MAINTAINER docker@kala.li


# Set up Prerequisites
WORKDIR /Kala2X_Bot
RUN apt-get update
RUN apt-get install -y ffmpeg python3-pip git

# Get Bot-Code from local Folder
ADD . /Kala2X_Bot/webm2mp4
WORKDIR /Kala2X_Bot/webm2mp4

# Set up Bot Requirements
RUN pip3 install --user -r requirements.txt

#Define ENV_Vars
ENV FFMPEG_THREADS 2
ENV FFMPEG_TIMELIMIT 900
ENV FFMPEG_PRESET slower
ENV TMP_PATH /tmp/
ENV TELEGRAM_TOKEN CHANGE_ME!

# Setting Bot ENTRYPOINT
ENTRYPOINT ["/Kala2X_Bot/webm2mp4/bot.py"]
