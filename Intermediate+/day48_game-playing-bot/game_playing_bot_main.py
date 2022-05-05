from selenium import webdriver

chrome_driver_path = ""
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.amazon.com")
