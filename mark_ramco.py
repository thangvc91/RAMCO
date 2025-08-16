from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
chrome_options = Options()
# chrome_options.add_argument(r'--user-data-dir=C:\Users\admin\AppData\Local\Google\Chrome\User Data\Profile 1')  # Path to your Chrome profile
chrome_options.add_argument(r'--user-data-dir=C:\Users\congthang.van\AppData\Local\Google\Chrome\User Data\Default')  # Path to your Chrome profile

# Optionally, specify your profile directory if you use multiple profiles:
# chrome_options.add_argument(r'--profile-directory=Default')  # Or 'Profile 1', etc.

driver = webdriver.Chrome(options=chrome_options)
# Set up the driver (make sure you have the correct driver for your browser)
# driver = webdriver.Chrome()  # or webdriver.Firefox(), etc.
wait = WebDriverWait(driver, 20)
from datetime import date 
def is_sunday():
    today = date.today()
    return today.weekday() == 6  # 6 corresponds to Sunday
if not is_sunday():
# Open the target webpage
    driver.get("https://ramcoasean.concentrix.com/")
    time.sleep(10)
    username_buttons = driver.find_elements(By.XPATH, "//button[@aria-label='Passwordless users, login here.']")

    # Click the button
    username_buttons[1].click()
    time.sleep(2)  # Wait for the login form to appear

    username_input = driver.find_element(By.ID, "username")
    # username_input.send_keys("congthang.van@concentrix.com")
    username_input.send_keys("duyliem.nguyen@concentrix.com")


    next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Next')]")))
    next_button.click()

    time.sleep(3)  # Wait for the next page to load

    login_div = driver.find_element(By.XPATH, "//div[text()='Login with CNX ADFS (external IDP)']")
    login_div.click()
    time.sleep(5)  # Wait for the next page to load
    # time.sleep(3)  # Wait for the next page to load


    password_input = driver.find_element(By.ID, "passwordInput")
    # password_input.send_keys("Romances12345678!@#$%^&*")
    password_input.send_keys("Tichcuc##me20242024limchin95")
    time.sleep(3)  # Wait for the next page to load



    sign_in_button = driver.find_element(By.ID, "submitButton")
    sign_in_button.click()
    time.sleep(30)  # Wait for the next page to load
    # Locate the element by its ID
    # element = driver.find_element(By.ID, "btnhrbook1_inbtn-button-1545-btnInnerEl")
    try:
        # Wait for the element to be clickable
        # in_button = wait.until(EC.element_to_be_clickable((By.ID, "btnhrbook1_inbtn-button-1545-btnInnerEl")))
        in_button = driver.find_element(By.ID, "btnhrbook1_inbtn-button-1545-btnInnerEl")
        # print(in_button.text)  # Print the text of the button to verify it's correct
        in_button.click()
    except Exception as e:
        print(f"An error occurred: {e}")
    try:
        # Wait for the element to be clickable
        time.sleep(5) 
        # in_button = wait.until(EC.element_to_be_clickable((By.ID, "btnhrbook1_inbtn-button-1545-btnInnerEl")))
        in_button = driver.find_element(By.ID, "btnhrbook1_inbtn-button-1545-btnInnerEl")
        # print(in_button.text)  # Print the text of the button to verify it's correct
        in_button.click()
    except Exception as e:
        print(f"An error occurred: {e}")
    driver.quit()
# Click the element
# element.click()

# Optional: close the browser
# driver.quit()
