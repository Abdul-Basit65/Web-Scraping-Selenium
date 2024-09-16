from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # Import Keys

path= "C:/Users/Shekhani Laptop/Downloads/New folder (12)/chromedriver-win64/chromedriver.exe"
s = Service(path)
driver = webdriver.Chrome(service=s)  # Note: 'service' is in lowercase
driver.get("https://www.google.com/")

# Locate the search box using the new syntax
box = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")

# Send keys to the search box
box.send_keys("House Of Dragon")
#Enter A Key
box.send_keys(Keys.ENTER)  # Correct (capital 'Keys')


box = driver.find_element(By.XPATH,"/html/body/div[3]/div/div[13]/div[4]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div[3]/div[8]/div/div/div/div/div/div[1]/div/div/span/a/h3").click()
driver.save_screenshot("C:/Users/Shekhani Laptop/Downloads/Python Web Scraping/Selenium/ss1.png")