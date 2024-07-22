# YouTube Downloader

This Python script downloads videos from YouTube using the `pytube` library. It allows you to download videos by providing a URL, selecting the desired resolution, and specifying the download path.

## Installation

1. **Install `pytube`:**

   ```bash
   pip install pytube
   ```

## Usage

1. **Run the script:**

   ```bash
   python youtube_downloader.py
   ```

2. **Follow the prompts:**

   - Enter the YouTube video URL.
   - Enter the download path where the video should be saved.
   - Select the desired resolution by typing the corresponding number.

## Troubleshooting
you may encounter thsi error:
`get_throttling_function_name: could not find match for multiple`

In cipher.py locate:
```python
r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&.*?\|\|\s*([a-z]+)',
r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])?\([a-z]\)',
```

And replace by:
```python
r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&.*?\|\|\s*([a-z]+)',
r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])\([a-z]\)',
```

This solution was on a comment from pytube issue #1750 on github
[https://github.com/pytube/pytube/issues/1750#issuecomment-1672185669](https://github.com/pytube/pytube/issues/1750#issuecomment-1672185669)