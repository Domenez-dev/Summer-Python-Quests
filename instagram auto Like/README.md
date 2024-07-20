# Instagram Auto Like Bot

This Python script automatically likes posts on an Instagram profile. It opens a Chrome browser, navigates to the specified Instagram profile, and likes a number of posts as specified by the user. The bot uses Selenium for browser automation and PyAutoGUI for mouse control.

## Features

- Automatically likes posts on an Instagram profile.
- Configurable settings through a `settings.ini` file.
- Allows specifying the number of posts to like.
- Supports adjusting the speed of the automation process.

## Prerequisites

- Python 3.6 or higher
- Chrome browser
- ChromeDriver compatible with your version of Chrome
- Required Python packages (listed below)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/instagram-auto-like-bot.git
   cd instagram-auto-like-bot
   ```

2. **Install required Python packages:**

   You can use `pip` to install the necessary packages. Run:

   ```bash
   pip install -r requirements.txt
   ```

3. **Download ChromeDriver:**

   - Download the ChromeDriver version that matches your Chrome version from [ChromeDriver download](https://sites.google.com/a/chromium.org/chromedriver/downloads).
   - Place the `chromedriver` executable in a directory and note the path.

## Usage

1. **Run the script:**

   Execute the Python script using:

   ```bash
   python clicks.py
   ```

2. **Follow the prompts:**

   - Enter the Instagram username of the profile you want to like posts from.
   - Enter the number of posts you want to like.

3. **Stop the script (if needed):**

   - Press `Esc` on your keyboard to stop the script.

## Configuration

- **`settings.ini`**: Contains configuration settings for Chrome and the speed factor.
  - `user_data_dir`: Path to your Chrome user data directory.
  - `profile_directory`: Name of the Chrome profile to use.
  - `driver_path`: Path to the `chromedriver` executable.
  - `speed`: Multiplier for the delay times (e.g., `1.0` for normal speed, `0.5` for faster).

## Note!:
- This script was made for chrome only, if you want to add other broswers you can issue it and I will assign you to do it
- This script was tested and worked correctly on `Windows`, with monitor resolution `1920 * 1080`, it is meant to be responsive the other resolutions but if you countered any problem with the mouse pointer you can issue it and be sure to mention the screen resolution used
- This script is for educational purposes only. Please use it responsibly and at your own risk.

## Troubleshooting

- **NoSuchElementException**: Ensure that the XPath for the like button matches the current Instagram HTML structure. Update the XPath if Instagram changes its layout.
- **ChromeDriver Error**: Ensure that the ChromeDriver version matches your installed Chrome version and that the path to `chromedriver` is correctly set in `settings.ini`.
- **Extensions Error**: If Chrome extensions cause issues, ensure that `--disable-extensions` is included in the Chrome options.
