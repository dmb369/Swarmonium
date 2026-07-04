# synth_engine.py

import pygame
import numpy as np
import os
from config import NOTE_FREQUENCIES

SAMPLE_RATE = 44100


class SynthEngine:
    def __init__(self, volume=0.5):
        pygame.mixer.init(frequency=SAMPLE_RATE, size=-16, channels=2, buffer=512)

        self.volume = volume
        self.active_notes = {}
        self.instrument = None

        self.base_array = None
        self.base_freq = None

    # -----------------------------
    # Instrument Loading
    # -----------------------------

    def load_instrument(self, name):
        self.instrument = name

        if name == "harmonium":
            path = os.path.join("sounds", "harmonium", "base.wav")
            self.base_freq = NOTE_FREQUENCIES["C4"]

        elif name == "guitar":
            path = os.path.join("sounds", "guitar", "A_string.wav")
            self.base_freq = NOTE_FREQUENCIES["A4"]

        else:
            return

        sound = pygame.mixer.Sound(path)
        self.base_array = pygame.sndarray.array(sound).astype(np.float32)

        print(f"Loaded instrument: {name}")

    # -----------------------------
    # Volume Handling
    # -----------------------------

    def set_volume(self, volume):
        self.volume = max(0.0, min(1.0, volume))

        for sound in self.active_notes.values():
            sound.set_volume(self.volume)

    # -----------------------------
    # Pitch Shifting
    # -----------------------------

    def pitch_shift(self, target_note):
        target_freq = NOTE_FREQUENCIES[target_note]
        ratio = target_freq / self.base_freq

        original_len = len(self.base_array)
        new_len = int(original_len / ratio)

        old_indices = np.arange(original_len)
        new_indices = np.linspace(0, original_len - 1, new_len)

        left = np.interp(new_indices, old_indices, self.base_array[:, 0])
        right = np.interp(new_indices, old_indices, self.base_array[:, 1])

        pitched = np.column_stack((left, right)).astype(np.int16)

        return pygame.sndarray.make_sound(pitched)

    # -----------------------------
    # Note Control
    # -----------------------------

    def play_note(self, note):
        if note in self.active_notes:
            return

        sound = self.pitch_shift(note)
        sound.set_volume(self.volume)
        sound.play(-1)
        self.active_notes[note] = sound

    def stop_note(self, note):
        if note in self.active_notes:
            self.active_notes[note].stop()
            del self.active_notes[note]
