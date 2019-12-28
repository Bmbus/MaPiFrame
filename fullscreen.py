from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://127.0.0.1:8080/#")


b = driver.find_elements_by_id("view-fullscreen")[0]
b.click()