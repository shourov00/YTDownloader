## Simple YouTube video downloader

This script allows you to download YouTube videos easily using Python.

## Installation

1. Create a virtual environment (if you're new to Python):

    ```bash
    python -m venv venv
    ```

2. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

3. Install required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Download YouTube video

Execute `main.py` with a YouTube video URL:

```bash
python main.py --url "youtube_video_url"
```

### Specify output path
You can specify the output path where the video will be downloaded:

```bash
python main.py --url "youtube_video_url" -o "C:/Users/my_pc/Downloads"
```

### Check available commands
```bash
python main.py --help
```

## Contributing
If you'd like to contribute to this project, please fork the repository, create a new branch, and make your changes. Afterward, submit a pull request for review.



