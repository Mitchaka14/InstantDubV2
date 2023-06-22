# ./voiceAndTranslation/VoiceTranslationClass.py

import os
from vocal_separation import separate_vocals


class VoiceTranslation:
    def __init__(self):
        self.input_audio_path = "OriginalAudio.mp3"  # Input audio file
        self.output_audio_dir = "./splitAudio"  # Output directory

    def process(self):
        if os.path.exists(self.input_audio_path):
            separate_vocals(self.input_audio_path, self.output_audio_dir)
            print("Vocal separation completed.")
        else:
            print(
                "OriginalAudio.mp3 not found. Please check the file path and try again."
            )


if __name__ == "__main__":
    vt = VoiceTranslation()
    vt.process()
