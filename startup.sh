#!/bin/bash

echo Starting Telegram Bot

chmod +x test.py
python3 test.py
echo telegram bot crashed
# Dummy ping for diagnosing Container
ping google.ch
