from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from fake_useragent import UserAgent
import time

# Generate a random user-agent
ua = UserAgent()
random_user_agent = ua.random
print(f"Using User-Agent: {random_user_agent}")

# Set Chrome options
chrome_options = Options()
chrome_options.add_argument(f"user-agent={random_user_agent}")  # Set fake user-agent
chrome_options.add_argument("--headless")  # Run in headless mode (optional)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Avoid detection
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)

service = Service(executable_path="/home/ajiri/project/aviationDataAnalysis/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://google.com")
print("Current User-Agent:", driver.execute_script("return navigator.userAgent;"))

time.sleep(10)

driver.quit()