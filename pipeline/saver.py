import os


def save_audio(audio, filename, formats, output_path):
    # saves the processed audio into multiple formats
    os.makefirs(output_path, exist_ok=True)

    for fmt in formats:
        output_file = os.path.join(output_path, f"{filename}.{fmt}")
        audio.export(output_file, format=fmt)
        print(f"Saved: {output_file}")
