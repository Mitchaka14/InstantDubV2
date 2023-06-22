from pytube import YouTube
import os
import shutil


def download_or_copy(source, output_dir_name=None):
    base_output_dir = "downloads/"

    # If no output directory name is provided, get name from source
    if not output_dir_name:
        if "youtube.com" or "youtu.be" in source:
            output_dir_name = YouTube(source).title
        else:
            output_dir_name = os.path.basename(source).rsplit(".", 1)[0]

    # Generate output directory path
    output_dir = os.path.join(base_output_dir, output_dir_name)

    # Check if output directory exists, if not, create it
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    else:
        # If directory already exists, add suffix
        count = 1
        while os.path.exists(output_dir + str(count)):
            count += 1
        output_dir = output_dir + str(count)

    # If source is a YouTube link
    if "youtube.com" or "youtu.be" in source:
        try:
            yt = YouTube(source)
            video = yt.streams.get_highest_resolution()
            video.download(output_dir)
            # Rename the video file to "OriginalVideo"
            video_file_path = os.path.join(output_dir, video.default_filename)
            renamed_file_path = os.path.join(output_dir, "OriginalVideo.mp4")
            os.rename(video_file_path, renamed_file_path)
            return True, "Download successful.", output_dir
        except Exception as e:
            return False, str(e), None
    else:
        # If source is a local file path
        try:
            shutil.copy2(source, output_dir)
            # Rename the file to "OriginalVideo"
            file_name = os.path.basename(source)
            renamed_file_path = os.path.join(
                output_dir, "OriginalVideo" + os.path.splitext(file_name)[1]
            )
            os.rename(os.path.join(output_dir, file_name), renamed_file_path)
            return True, "File copy successful.", output_dir
        except Exception as e:
            return False, str(e), None


if __name__ == "__main__":
    result, message, output_dir = download_or_copy("your source here")
    print(message)
