# 🎹 Swarmonium

**One sample. Infinite notes.**

Swarmonium is a virtual instrument studio that turns your computer keyboard into a playable harmonium or guitar — without a single extra recording. Feed it one sampled note, and it pitch-shifts that sample in real time to cover a full scale, live, as you play.

No sample library. No MIDI rig. Just one `.wav` file, a bit of math, and your QWERTY row.

---

## ✨ Features

- **Two instruments, one engine** — switch instantly between **Harmonium** and **Guitar** with `TAB`
- **Real-time pitch shifting** — a single base sample (`C4` for harmonium, `A4` for guitar) is resampled on the fly via NumPy interpolation to produce every note in the scale
- **Two-row keyboard layout** — white keys and black keys mapped like a mini piano
- **Live volume control** — hold `↑` / `↓` to fade in or out mid-performance
- **Clean, animated UI** — gradient backdrop, live volume bar, and real-time display of pressed keys and sounding notes
- **Lightweight** — built entirely on `pygame` + `numpy`, no heavyweight audio engine required

---

## 🎮 Controls

| Key(s) | Action |
|---|---|
| `Z X C V B N M` | White keys — A4 through G4 |
| `S D G H` | Black keys — A#4, C#4, D#4, F#4 |
| `TAB` | Switch between Harmonium and Guitar |
| `↑` / `↓` (hold) | Increase / decrease volume |
| `ESC` | Quit |

The on-screen display shows the currently pressed keys and which notes are actively sounding, along with a live volume meter.

---

## 🧠 How It Works

Most virtual instruments rely on a full bank of pre-recorded samples — one per note, per instrument. Swarmonium takes a different approach:

1. **One base sample** is loaded per instrument (a single harmonium drone or a single guitar string pluck).
2. When you press a key, the engine calculates the **frequency ratio** between the target note and the base sample's known frequency.
3. That ratio is used to **resample the waveform** (via `numpy.interp`) — stretching or compressing it in time, which raises or lowers its pitch.
4. The freshly pitch-shifted sound is played back through `pygame.mixer` in real time, looped for as long as the key is held.

This is the same core idea behind classic hardware/software samplers: record once, play anywhere on the keyboard.

```
target_frequency / base_frequency = pitch ratio
new_sample_length = original_length / pitch ratio
```

---

## 📁 Project Structure

```
swarmonium/
├── main.py              # App loop, UI rendering, input handling
├── synth_engine.py       # Core pitch-shifting + playback engine
├── config.py             # Window settings, key mappings, note frequencies
├── requirements.txt
└── sounds/
    ├── harmonium/
    │   └── base.wav       # Base harmonium sample (C4)
    └── guitar/
        └── A_string.wav   # Base guitar sample (A4)
```

---

## 🚀 Getting Started

### Requirements
- Python 3.8+
- `pygame`
- `numpy`

### Installation

```bash
git clone https://github.com/yourusername/swarmonium.git
cd swarmonium
pip install -r requirements.txt
```

### Run it

```bash
python main.py
```

A window will open — start pressing keys to play!

---

## 🛠️ Roadmap

Some ideas for where this could go next:

- [ ] Sustain pedal / ADSR envelope shaping
- [ ] More instruments (sitar, flute, tabla?)
- [ ] Chord recording and playback
- [ ] MIDI input support
- [ ] Adjustable octave range
- [ ] Export played sessions to `.wav`

---

## 🤝 Contributing

Pull requests, new instrument samples, and UI polish are all welcome. If you add a new instrument, drop a single base `.wav` sample in `sounds/<name>/` and register it in `synth_engine.py`.

---

## 📜 License

MIT — do whatever you'd like with it, just keep the tune going.

---

*Built for anyone who ever wanted a harmonium at 2am but only had a laptop.*
