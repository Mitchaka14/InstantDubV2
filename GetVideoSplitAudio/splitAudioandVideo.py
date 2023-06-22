# splitAudioandVideo
from moviepy.editor import VideoFileClip
import os


def split_video_audio(filepath):
    try:
        # Load video using moviepy
        clip = VideoFileClip(filepath)

        # Extract audio
        audio = clip.audio
        audio_filename = os.path.join(
            os.path.dirname(filepath), "OriginalAudio" + ".mp3"
        )
        audio.write_audiofile(audio_filename)

        return True, "Audio separation successful."
    except Exception as e:
        return False, str(e)


if __name__ == "__main__":
    result, message = split_video_audio("your filepath here")
    print(message)
