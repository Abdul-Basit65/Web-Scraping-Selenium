from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import random
from fake_useragent import UserAgent

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--disable-gpu")  # Disable GPU to avoid GPU errors
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

# Use a random user-agent to avoid detection
ua = UserAgent()
chrome_options.add_argument(f"user-agent={ua.random}")

# Provide the full path to the ChromeDriver
chrome_driver_path = "C:/Users/Shekhani Laptop/Downloads/New folder (12)/chromedriver-win64/chromedriver.exe"

# Create a Service object with the path to ChromeDriver
service = Service(executable_path=chrome_driver_path)

# Initialize the WebDriver using the Service object
driver = webdriver.Chrome(service=service, options=chrome_options)

# Example: Open Yelp
driver.get('https://www.yelp.com/search?find_desc=restaurants&find_loc=New+York%2C+NY')

# Simulate human-like behavior with scrolling and random waits
time.sleep(random.uniform(3, 6))  # Random sleep before interacting with the page

# Scroll down the page randomly to simulate a human user
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(random.uniform(5, 10))  # Random wait between 5 to 10 seconds

# Check if CAPTCHA is present (you may have to solve it manually)
input("Please solve the CAPTCHA manually if prompted, then press Enter to continue...")

# Example action: Print the title of the page to confirm it loaded
print(driver.title)

# Additional scraping logic goes here, for example:
# restaurants = driver.find_elements_by_class_name('businessName')
# for restaurant in restaurants:
#     print(restaurant.text)

# Close the browser when done
driver.quit()
