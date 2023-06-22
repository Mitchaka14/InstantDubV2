# ./main.py

import os
import sys

sys.path.append(
    "./GetVideoSplitAudio"
)  # Add the path to the scripts in the GetVideoSplitAudio folder
sys.path.append(
    "./voiceAndTranslation"
)  # Add the path to the scripts in the voiceAndTranslation folder

from GetVideoSplitAudio.GVSA_class import Video
from voiceAndTranslation.VoiceTranslationClass import VoiceTranslation


def main():
    # a youtube link or a file path
    # optionally also accepts name for dir
    v = Video("https://youtu.be/E6-V86n61Qg", "withVoice")
    result, message = v.process()
    print(message)

    # Now let's proceed to vocal separation
    vt = VoiceTranslation()
    vt.process()


if __name__ == "__main__":
    main()
