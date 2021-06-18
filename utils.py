import json
import os
import random
import string

from hurry.filesize import alternative, size


def bytes2human(raw):
    return size(raw, system=alternative)

def filesize(filename):
    return os.stat(filename).st_size

def load_config_vars():
    # Config Dictionary init
    config = {"telegram_token": ""}

    # Loading ENV Vars from Docker
    telegram_token = os.environ['TELEGRAM_TOKEN']
    ffmpeg_threads = os.environ['FFMPEG_THREADS']
    temp_path = os.environ['TMP_PATH']
    ffmpeg_timelimit = os.environ['FFMPEG_TIMELIMIT']
    ffmpeg_preset = os.environ['FFMPEG_PRESET']

    if ffmpeg_threads != "":
     print(f"FFMPEG Threads not set, defaulting to 2 Threads.")
     ffmpeg_threads = 2

    if temp_path != "":
     print(f"Temp Path not set, defaulting to /tmp/.")
     temp_path = "/tmp/"

    if ffmpeg_timelimit !="":
     print(f"FFMPEG Timelimit not set, defaulting to 15 CPU Minutes.")
     ffmpeg_timelimit = 900

    if ffmpeg_preset !="":
     print(f"FFMPEG Preset is not set, defaulting to 'veryfast' Preset.")
     ffmpeg_preset = "veryfast"

     print('Using the following Parameters: FFMPEG Threads: ' + str(ffmpeg_threads) + ', Temp Path: ' + str(temp_path) + ', Telegram Bot Token: ' + str(telegram_token) + '.')

     for variable in ["telegram_token", "ffmpeg_threads", "temp_path", "ffmpeg_timelimit", "ffmpeg_preset"]:
         config[variable] = eval(variable)
     return config

def load_config(filename):
    # Default config
    config_json = {"telegram_token": "",
              "ffmpeg_threads": 2,
              "temp_path": "/tmp/",
              "ffmpeg_timelimit": 900,
              "ffmpeg_preset": "veryfast"}
    try:
        with open(filename, "r") as f:
            config.update(json.load(f))
        return config
    except FileNotFoundError:
        with open(filename, "w") as f:
            json.dump(config, f, indent=4)
            return config
    except:
        print(f"Unable to parse {filename}, is it corrupted?")
        exit(1)


def rm(filename):
    """Delete file"""
    try:
        os.remove(filename)
    except Exception as e:
        print(f"Unable to rm {filename}: {e}")


def random_string(length=12):
    """Random string of uppercase ASCII and digits"""
    return "".join(
        random.choice(string.ascii_uppercase + string.digits) for _ in range(length)
    )

