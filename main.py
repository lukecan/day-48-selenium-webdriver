from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import time

# Setting the time for the cookie-clicking loop to run for 5 minutes
five_min = time() + 60 * 5

# Setting the path to the ChromeDriver
chrome_driver_path = "./chromedriver"
service = Service(chrome_driver_path)

# Starting a ChromeDriver session
driver = webdriver.Chrome(service=service)

# URL to the cookie-clicking game
URL = "http://orteil.dashnet.org/experiments/cookie/"

# Navigating to the game
driver.get(URL)

# Finding the cookie element on the page
cookie = driver.find_element(by=By.ID, value="cookie")

# Loop for clicking the cookie every 5 seconds
timeout = time() + 5
while True:
    cookie.click()
    if time() > timeout:
        # Finding all the items in the store, excluding the last item (which is the store's title)
        shopping_cart = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")[:-1]

        # Creating a list of items that can be bought (not grayed out)
        to_buy = [item for item in shopping_cart if item.get_attribute("class") != "grayed"]

        # Buying the last item in the list
        to_buy[-1].click()

        # Resetting the timeout
        timeout = time() + 5

        # Exiting the loop after 5 minutes
        if time() > five_min:
            print(driver.find_element(By.ID, value="cps").text)
            break
