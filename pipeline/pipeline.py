import yaml
from .loader import load_audio_files
from .transforms import apply_effects
from .saver import save_audio


def run_pipeline(config_path="config/config.yaml"):
    # reads config, loads audio files, applies effects, saves output

    # Load YAML
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    audio_files = load_audio_files(config["input_path"])

    for filename, audio in audio_files:
        print(f"Processing {filename}...")

        processed = apply_effects(audio, config["effects"])

        base_name = filename.split(".")[0]
        save_audio(
            processed, base_name, config["output_formats"], config["output_path"]
        )

    print("Pipeline completed successfully!")
