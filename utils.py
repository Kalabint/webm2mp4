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
    config = {"telegram_token": "",
              "ffmpeg_threads": 2,
              "temp_path": "/tmp/",
              "ffmpeg_timelimit": 900,
              "ffmpeg_preset": "slow"}

    # Loading ENV Vars from Docker
    telegram_token = os.getenv('TELEGRAM_TOKEN') or ''
    ffmpeg_threads = os.getenv('FFMPEG_THREADS') or ''
    temp_path = os.getenv('TMP_PATH') or ''
    ffmpeg_timelimit = os.getenv('FFMPEG_TIMELIMIT') or ''
    ffmpeg_preset = os.getenv('FFMPEG_PRESET') or ''

    print('Using the following Parameters: FFMPEG Timelimit: ' + str(ffmpeg_timelimit) + ', FFMPEG Preset: ' + str(ffmpeg_preset) + ', FFMPEG Threads: ' + str(ffmpeg_threads) + ', Temp Path: ' + str(temp_path) + ', Telegram Bot Token: ' + str(telegram_token) + '.')

    for variable in ["telegram_token", "ffmpeg_threads", "temp_path", "ffmpeg_timelimit", "ffmpeg_preset"]:
        config[variable] = eval(variable)
    return config

def load_config(filename):
    # Default config
#    config_json = {"telegram_token": "",
#              "ffmpeg_threads": 2,
#              "temp_path": "/tmp/",
#              "ffmpeg_timelimit": 900,
#              "ffmpeg_preset": "veryfast"}
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

