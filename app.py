import sys
import random
import pathlib
import argparse
import keyboard
import threading
import playsound

def parse_arguments(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('--log', default=False, action='store_true')
    parser.add_argument('--shuffle', default=False, action='store_true')
    return parser.parse_args(args)

def import_keys(switches):
    keys_path = [p for p in pathlib.Path(f'switches/{switches}').iterdir() if p.is_file()]
    key_dict = {}

    for key_path in keys_path:
        key_dict[key_path.stem] = key_path.as_posix()

    return key_dict

def play_key_sound(key):
    if args.shuffle or key.lower() not in key_dict:
        fallback_key = random.choice(list(key_dict.values()))   # Randomly select a sound for unassigned keys
        playsound.playsound(fallback_key)

    elif key.lower() in key_dict:
        playsound.playsound(key_dict[key.lower()])

def onkeypress(event):
    threading.Thread(target=play_key_sound, args=(event.name,), daemon=True).start()
    if args.log: print(event.name)

def print_switch_menu():
    options = [d.stem for d in pathlib.Path('switches/').iterdir() if d.is_dir()]

    print('\nSelect the preferred switch sound by typing its index:')
    
    for i, option in enumerate(options):
        print(f'{i+1}. {option}')

    try:
        selection = int(input('\nSelect a switch: '))
        return options[selection - 1]
    
    except IndexError:
        sys.exit(0)

def start_emulating():
    keyboard.on_press(onkeypress)   # Register keypress listener
    print(f'\nEmulating {switches} switches! CTRL+C anytime to stop.')

    while True:
        pass

args = parse_arguments(sys.argv[1:])

switches = print_switch_menu()
key_dict = import_keys(switches)
start_emulating()