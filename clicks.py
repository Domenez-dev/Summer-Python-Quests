import pyautogui
import time
import random
import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

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
chrome_options.add_argument("user-data-dir=C:\\Users\\Zakkye\\AppData\\Local\\Google\\Chrome\\User Data")  # Change this to your user data directory
chrome_options.add_argument("profile-directory=Profile 1")  # Change this to your profile directory name
chrome_options.add_argument("--disable-extensions")  # Disable extensions
chrome_options.add_argument("--remote-debugging-port=9222")  # Enable remote debugging
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")

# Initialize the WebDriver
driver_path = 'chromedriver/chromedriver.exe'
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
time.sleep(3)  # Wait for the page to load

# Navigate to the specified user's profile (replace with the desired username)
profile_url = 'https://www.instagram.com/usthb_university/'  # Replace with the actual profile URLs
driver.get(profile_url)
time.sleep(3)

# Get the number of posts
num_posts_elem = driver.find_element(By.XPATH, "//span[@class='_ac2a']")
num_posts = int(num_posts_elem.text.replace(',', ''))
print(f'Total number of posts: {num_posts}')

# Prompt the user for the number of posts to like
# num_to_like = int(input(f'Enter the number of posts you want to like (max {num_posts}): '))
num_to_like = 5

# Like the specified number of posts
for _ in range(num_to_like):
    if stop_flag:
        break

    # Find the first post and click it to open
    if _ == 0:
        first_post = driver.find_element(By.XPATH, "//div[@class='_aagw']")
        first_post.click()
        time.sleep(1)

    # Ensure the post is fully loaded
    time.sleep(1)
    
    try:
        # Locate the like button using Selenium
        like_button = driver.find_element(By.XPATH, "//span[@class='x1rg5ohu xp7jhwk']")
        
        # Get the location of the like button
        location = like_button.location
        size = like_button.size

        # Calculate the coordinates to click on
        x = location['x'] + 220
        y = location['y'] + 330

        # Move the mouse to the like button and click it
        pyautogui.moveTo(x, y)
        pyautogui.click()

        print(f"Liked post {_ + 1}")

    except Exception as e:
        print(f"Error liking post {_ + 1}: {e}")

    # Navigate to the next post using the right arrow key
    if _ < num_to_like - 1:
        pyautogui.press('right')
        time.sleep(1)

print("Done!")

# Close the browser
driver.quit()
