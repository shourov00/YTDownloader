import sys
import time

import pytube

start_time = time.time()


def download_yt_video(video_url, output_path):
    # get youtube object
    yt = pytube.YouTube(video_url, on_progress_callback=progress_func, on_complete_callback=completed_function)

    # get the highest resolution video stream & thumbnail
    stream = yt.streams.get_highest_resolution()

    # download yt video
    print(f'Downloading {stream.title} ({format(stream.filesize_mb, ".2f")} MB)')
    stream.download(output_path=output_path, max_retries=1)


def progress_func(stream, chunk, bytes_remaining):
    bytes_downloaded = stream.filesize - bytes_remaining
    done = int(50 * bytes_downloaded / stream.filesize)

    # Calculate elapsed time
    elapsed_time = time.time() - start_time

    # Calculate download speed in kilobytes per second (KB/s)
    speed = (bytes_downloaded / 1024) / elapsed_time if elapsed_time > 0 else 0
    speed_color = "\033[91m"  # red color
    eta_color = '\033[96m'  # cyan color
    reset_color = "\033[0m"

    # Calculate remaining time (ETA) in seconds
    if speed > 0:
        eta = bytes_remaining / (speed * 1024)
    else:
        eta = 0

    # Convert ETA to hours, minutes, and seconds
    eta_hours = int(eta / 3600)
    eta_minutes = int((eta % 3600) / 60)
    eta_seconds = int(eta % 60)

    sys.stdout.write("\r[{}{}] {:.1f}/{:.1f} MB {}{:.1f}{} kB/s eta {}{:02d}:{:02d}:{:02d}{} ".format(
        '=' * done, ' ' * (50 - done),
        bytes_downloaded / (1024 * 1024),
        stream.filesize / (1024 * 1024),
        speed_color, speed, reset_color,
        eta_color, eta_hours, eta_minutes, eta_seconds, reset_color
    ))
    sys.stdout.flush()


def completed_function(stream, file_path):
    print(f"Download completed \nFile at {file_path}")