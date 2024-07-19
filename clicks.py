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

# Initialize the WebDriver (make sure the path to the WebDriver is correct)
driver_path = 'path/to/chromedriver'
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Start the browser maximized

service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open Instagram and login (replace with your credentials)
driver.get('https://www.instagram.com/accounts/login/')
time.sleep(2)

username = driver.find_element(By.NAME, 'username')
password = driver.find_element(By.NAME, 'password')

username.send_keys('your_username')
password.send_keys('your_password')

login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

time.sleep(5)  # Wait for the login to complete

# Navigate to a post (replace with the URL of the post you want to like)
post_url = 'https://www.instagram.com/p/xxxxxxxxxxx/'
driver.get(post_url)
time.sleep(5)

# Locate the like button using Selenium
like_button = driver.find_element(By.XPATH, "//svg[@aria-label='Like']")

# Get the location of the like button
location = like_button.location
size = like_button.size

# Calculate the coordinates to click on
x = location['x'] + size['width'] / 2
y = location['y'] + size['height'] / 2

# Move the mouse to the like button and click it
pyautogui.moveTo(x, y, duration=1)
pyautogui.click()

print("Liked the post!")

# Close the browser
driver.quit()

# Run a loop with the ability to stop using the hotkey
for _ in range(10):  # Replace with the desired number of repetitions
    if stop_flag:
        break
    pyautogui.moveTo(x, y, duration=1)
    pyautogui.click()
    time.sleep(random.uniform(0.5, 1.5))

print("Done!")
