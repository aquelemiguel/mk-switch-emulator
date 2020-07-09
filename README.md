# mk-switch-emulator
A simple script which emulates mechanical keyboard switch sounds. Inspired by a [Glarses' video](https://www.youtube.com/watch?v=P_9vXJZVT54).

## Features
* Very low latency
* Asynchronous audio playing
* Support for multiple switch types
* Automatic key mapping by filename

## Installation
1. Install [Python 3.x](https://www.python.org/downloads/)
2. Download and unzip this repo
3. Install dependencies with `pip install -r requirements.txt`

## Usage
* Run `python app.py`

## Importing custom sounds
1. Ensure clip filenames follow the key names for your keyboard's layout (include `--log` flag to see pressed keys)
2. Extract your custom switch sounds to the `/switches` directory
3. Restart the script
