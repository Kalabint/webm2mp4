#!/bin/bash

# Setting up Config file with ENV-Vars
echo Checking Telegram Token...
if [ -z "$TELEGRAM_TOKEN" ]
	then
	echo Please define the TELEGRAM_TOKEN Variable
	else
	sed -i "s/"telegram_token": "",/"telegram_token": "$TELEGRAM_TOKEN",/g" ./config.json
fi

echo ffmpeg: $FFMPEG_THREADS
if [ -z "$FFMPEG_THREADS" ]
	then
	echo ENV FFMPEG_THREADS is undefined, falling back to default
	FFMPEG_THREADS=2
fi
	sed -i "s/"ffmpeg_threads" : 2,/"ffmpeg_threads" : $FFMPEG_THREADS,/g" ./config.json

echo Path: $TMP_PATH
if [ -z "$TMP_PATH" ]
	then
	echo ENV TMP_PATH is undefined, falling back to default
	TMP_PATH=/tmp/
fi
#	sed -i 's/"temp_path": "/\tmp/\"="temp_path": "$TMP_PATH"/g' config.json
	sed -i "s#"temp_path": "/tmp/"#"temp_path": "$TMP_PATH"#g" ./config.json

echo Starting Telegram Bot
echo
# Starting Telegram Bot
python3 bot.py
echo telegram bot crashed
ping google.ch
