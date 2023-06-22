# class
import os

try:
    from GetVideoSplitAudio.getVideo import download_or_copy
    from GetVideoSplitAudio.splitAudioandVideo import split_video_audio
except ImportError:
    from getVideo import download_or_copy
    from splitAudioandVideo import split_video_audio


# This is the main Video class that uses functions from script1 and script2.
class Video:
    # The constructor takes in a source (a YouTube link or local filepath) and an output directory.
    def __init__(self, source, output_dir_name=None):
        self.source = source
        self.output_dir_name = output_dir_name

    # The process method does all the work. It first calls the download_or_copy function to either download
    # the YouTube video or copy a local file into the output directory. It then calls the split_video_audio
    # function to split the video into separate audio and video files.
    def process(self):
        result, message, output_dir = download_or_copy(
            self.source, self.output_dir_name
        )
        print(message)
        if result:
            # Change here: use the new name "OriginalVideo" with the corresponding extension
            extension = (
                ".mp4"
                if "youtube.com" or "youtu.be" in self.source
                else os.path.splitext(self.source)[1]
            )
            filepath = os.path.join(output_dir, "OriginalVideo" + extension)
            result, message = split_video_audio(filepath)
            print(message)
            if result:
                return True, "Get video and audio completed"
        return False, "Process failed"


if __name__ == "__main__":
    v = Video("your source here")
    result, message = v.process()
    print(message)
