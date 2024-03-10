import argparse
import os

from downloader import download_yt_video

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download YouTube video.")
    parser.add_argument("--url", "-u", help="URL of the YouTube video")
    parser.add_argument("--output", "-o", help="Output path")
    args = parser.parse_args()

    if not args.url:
        parser.error("URL is required. Please provide a YouTube video URL using --url or -u option.")
        parser.print_help()
        exit()

    if args.output:
        output_path = args.output
    else:
        output_path = os.path.join(os.getcwd(), "downloads")  # Default output path

    download_yt_video(args.url, output_path)
