
# "🎄 Magical Christmas Audio Processor"
---
### Using **PyDub**, **PyYAML**, and **FFmpeg**  
This project applies a **Magical Christmas Storytelling** audio effect chain to any input audio.  
You used it specifically with **audio_1.wav** and **audio_2.mp3**, applying the “Magical Christmas storytelling tone” preset.

---

##  1. Requirements (MOST IMPORTANT PART)
To run this project successfully, you **must install FFmpeg**.  
PyDub *depends* on FFmpeg for reading/decoding and exporting audio formats.

###  Install FFmpeg
macOS
```
brew install ffmpeg
```
Linux
```
sudo apt install ffmpeg
```
---
## 2. Magical Christmas Storytelling Tone
```
effects:
  - name: "eq"
    low_gain: -3
    mid_gain: +2
    high_gain: +4

  - name: "pitchshift"
    semitones: +3
    formant_shift: +1

  - name: "chorus"
    rate: 0.8
    depth: 0.4
    mix: 0.2

  - name: "reverb"
    room_size: 0.55
    mix: 0.35

  - name: "delay"
    time: 120
    feedback: 0.15
    mix: 0.10
```
---

## 3. The Main Script Logic

```
transforms.py
````
does the following:

- Loads effects.yaml using PyYAML
- Loads each input audio using PyDub
- Applies effects in the order listed
- Saves output to /output as WAV

---

## 4. Summary


This project demonstrates:

- How to parse audio effect chains using PyYAML
- How to apply processing with PyDub
- How to support dynamic pipelines using YAML configs
- Handling FFmpeg installation (critical for PyDub)

---

 Perfect for immersive storytelling, whimsical character voices, cozy bedtime tales, enchanted fantasy narration, playful kids’ audio adventures, and any project that needs a touch of magic and personality 🎧 !

---
