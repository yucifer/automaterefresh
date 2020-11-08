import time
from selenium import webdriver


# Enter path to your chromdriver in webdriver.Chrome('PATH WHERE THE CHROMEDRIVER IS LOCATED')
driver = webdriver.Chrome('./chromedriver')

# Enter the URL of the website you want the browser to open and refresh after the specified time
driver.get("https://www.youtube.com")


while True:
    # Enter the time in seconds after which you want the page to be refreshed, here it will refresh after every 30 seconds.
    time.sleep(30)
    driver.refresh()  # Refreshes the webpage
