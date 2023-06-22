from GVSA_class import Video


# This function serves as a test function. It creates an instance of the Video class and calls its process method.
def test_video_class():
    # a youtube link or a file path
    # optionally also accepts name for dir
    v = Video("https://youtu.be/E6-V86n61Qg", "trial")
    result, message = v.process()
    print(message)


if __name__ == "__main__":
    # We simply call the test function when this script is run.
    test_video_class()
