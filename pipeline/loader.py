from pydub import AudioSegment
import os


def load_audio_files(input_path):
    # Loads all audio files from a directory.
    audio_files = []
    for filename in os.listdir(input_path):
        if filename.endswith(
            (".wav", ".mp3")
        ):  # output format as indicated in config file
            full_path = os.path.join(input_path, filename)
            audio = AudioSegment.from_file(full_path)
            audio_files.append((filename, audio))
    return audio_files
