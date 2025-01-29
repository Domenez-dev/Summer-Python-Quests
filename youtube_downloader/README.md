# YouTube Downloader

This Python repository provides tools to download videos from YouTube. It includes two versions:
1. **`yt-downloader.py`**: A version with a graphical user interface (GUI) built using Tkinter.
2. **`ytd-flask.py`**: A version with a web-based GUI built using Flask.

## Installation

1. **Install required libraries:**

   You can install the required libraries using:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Tkinter Version (`yt-downloader.py`)

1. **Run the script:**

   ```bash
   python yt-downloader.py
   ```

2. **Follow the GUI prompts:**

   - Enter the YouTube video URL.
   - Enter the download path where the video should be saved.
   - Select the desired resolution and format.

### Flask Version (`ytd-flask.py`)

1. **Run the Flask app:**

   ```bash
   python ytd-flask.py
   ```

2. **Open a web browser and navigate to:**

   ```
   http://127.0.0.1:5000
   ```

3. **Follow the web-based prompts:**

   - Enter the YouTube video URL.
   - Choose the download options (resolution and format).

## Troubleshooting

### Common Issues

If you encounter the following error:

```
get_throttling_function_name: could not find match for multiple
```

Follow these steps:

1. **Locate and modify `cipher.py`:**

   Find and replace:
   ```python
   r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&.*?\|\|\s*([a-z]+)',
   r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])?\([a-z]\)',
   ```

   With:
   ```python
   r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&.*?\|\|\s*([a-z]+)',
   r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])\([a-z]\)',
   ```

   This solution was provided in a comment on [pytube issue #1750 on GitHub](https://github.com/pytube/pytube/issues/1750#issuecomment-1672185669).
