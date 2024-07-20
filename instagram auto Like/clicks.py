import pyautogui
import time
import random
import keyboard
import configparser
from PIL import ImageGrab
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Load settings from the config file
config = configparser.ConfigParser()
config.read('settings.ini')

# Extract settings
user_data_dir = config.get('chrome', 'user_data_dir')
profile_directory = config.get('chrome', 'profile_directory')
driver_path = config.get('chrome', 'driver_path')
speed = float(config.get('speed', 'value'))

# Define the global stop flag
stop_flag = False

# Define the stop function
def stop_loop():
    global stop_flag
    stop_flag = True
    print("Stopping the loop...")

# Set up the hotkey to stop the loop
keyboard.add_hotkey('esc', stop_loop)

# Set up Chrome options to use a specific user profile
chrome_options = Options()
chrome_options.add_argument(f"user-data-dir={user_data_dir}")
chrome_options.add_argument(f"profile-directory={profile_directory}")
chrome_options.add_argument("--disable-extensions")  # Disable extensions
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")

# Initialize the WebDriver
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Prompt for the Instagram username
username = input('Enter the Instagram username you want to like posts from: ')

# Open Instagram and navigate to the specified user's profile
profile_url = f'https://www.instagram.com/{username}/'
driver.get(profile_url)
time.sleep(5 * speed)  # Wait for the page to load

# Get the number of posts
num_posts_elem = driver.find_element(By.XPATH, "//span[@class='_ac2a']")
num_posts = int(num_posts_elem.text.replace(',', ''))
print(f'Total number of posts: {num_posts}')

# Prompt the user for the number of posts to like
num_to_like = int(input(f'Enter the number of posts you want to like (max {num_posts}): '))

num_to_like = int(input(f'Enter the number of posts you want to like (max {num_posts}): '))

# Capture the screen
screen = ImageGrab.grab()

# Get screen size
screen_width, screen_height = screen.size

# Like the specified number of posts
for _ in range(num_to_like):
    if stop_flag:
        break

    # Find the first post and click it to open
    if _ == 0:
        first_post = driver.find_element(By.XPATH, "//div[@class='_aagw']")
        first_post.click()
        time.sleep(2 * speed)

    # Ensure the post is fully loaded
    time.sleep(2 * speed)
    
    try:
        # Locate the like button using Selenium
        like_button = driver.find_element(By.XPATH, "//span[@class='x1rg5ohu xp7jhwk']")
        
        # Get the location of the like button
        location = like_button.location
        size = like_button.size

        # Calculate the coordinates to click on
        x = location['x'] + screen_width * 11.45 / 100
        y = location['y'] + screen_height * 30.5 / 100

        # Move the mouse to the like button and click it
        pyautogui.moveTo(x, y)
        pyautogui.click()

        print(f"Liked post {_ + 1}")

    except Exception as e:
        print(f"Error liking post {_ + 1}: {e}")

    # Navigate to the next post using the right arrow key
    if _ < num_to_like - 1:
        pyautogui.press('right')
        time.sleep(2 * speed)

print("Done!")

# Close the browser
driver.quit()
