from pydub import AudioSegment
import os


def apply_bandpass(audio, low_freq, high_freq):
    # Applies a bandpass filter to the audio segment.
    filtered = audio.low_pass_filter(high_freq)
    filtered = filtered.high_pass_filter(low_freq)
    return filtered


def apply_pitchshift(audio, semitones):
    # simple pitch shifting using speed change approximation
    new_rate = audio.frame_rate * (2.0 ** (semitones / 12))
    shifted = audio.spawn(audio.raw_data, overrides={"frame_rate": int(new_rate)})
    return shifted.set_frame_rate(audio.frame_rate)


def apply__mixnoise(audio, volume=-20):
    # adds white noise to the audio
    noise = AudioSegment.silent(duration=len(audio))
    noise = noise.overlay(
        AudioSegment.white_noise(duration=len(audio)).apply_gain(volume)
    )
    return audio.overlay(noise)


def apply_effects(audio, effects_list):
    # applies effects showed in YAML config
    for effect in effects_list:
        if effect["name"] == "bandpass":
            audio = apply_bandpass(audio, effect["low_freq"], effect["high_freq"])

        elif effect["name"] == "pitchshift":
            audio = apply_pitchshift(audio, effect["semitones"])

        elif effect["name"] == "mixnoise":
            audio = apply__mixnoise(audio, effect["volume"])

    return audio
