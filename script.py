import time
import pyautogui

# Set the initial click speed
click_speed = 0.01  # Change this value to adjust the click speed

# Find the cookie image on the screen
cookie_image = 'goeie.png'  # Replace with your desired cookie image

# Main loop
while True:
    # Click on the cookie
    cookie = pyautogui.locateOnScreen(cookie_image)
    if cookie is not None:
        cookie_center = pyautogui.center(cookie)
        pyautogui.click(cookie_center)
        time.sleep(click_speed)
