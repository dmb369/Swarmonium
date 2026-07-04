# config.py

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
FPS = 60

INITIAL_VOLUME = 0.5
VOLUME_STEP = 0.6

KEY_MAP = {
    'z': "A4",
    'x': "B4",
    'c': "C4",
    'v': "D4",
    'b': "E4",
    'n': "F4",
    'm': "G4"
}

BLACK_KEY_MAP = {
    's': "A#4",
    'd': "C#4",
    'g': "D#4",
    'h': "F#4"
}

ALL_KEYS = {**KEY_MAP, **BLACK_KEY_MAP}

NOTE_FREQUENCIES = {
    "A4": 440.00,
    "A#4": 466.16,
    "B4": 493.88,
    "C4": 261.63,
    "C#4": 277.18,
    "D4": 293.66,
    "D#4": 311.13,
    "E4": 329.63,
    "F4": 349.23,
    "F#4": 369.99,
    "G4": 392.00,
}
