import time
from time import sleep

from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://qa-mesto.praktikum-services.ru/")
driver.add_cookie({"name": "my_first_cookie", "value": "15"})
cookie = driver.get_cookie("my_first_cookie")
assert cookie["value"] == "15"

driver.quit()
