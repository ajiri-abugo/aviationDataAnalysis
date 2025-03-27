#import libraries
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

ua = UserAgent()
random_user_agent = ua.random
#headers = {"User-Agent": ua.random}

options = Options()
options.set_preference("general.useragent.override", random_user_agent)  # Sets fake user-agent
options.set_preference("javascript.enabled", True)  # Enable JavaScript
# Optional: Remove headless mode to see browser interactions
#options.add_argument("--headless")  # Run in headless mode (optional)

# Set up WebDriver service (modify path if needed)
service = Service("/snap/bin/geckodriver")  # Adjust the path to match your system

# Start WebDriver
driver = webdriver.Firefox(service=service, options=options)

driver.get("https://www.qatarairways.com/en-eg/destinations/country.html")

# Print the User-Agent to confirm it's working
print("Current User-Agent:", driver.execute_script("return navigator.userAgent;"))

time.sleep(10)

driver.quit()