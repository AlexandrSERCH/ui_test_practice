from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://qa-mesto.praktikum-services.ru/")

# здесь добавь свой предыдущий код для добавления куки
driver.add_cookie({"name": "my_first_cookie", "value": "15"})
cookie = driver.get_cookie("my_first_cookie")

# а теперь измени значение куки
driver.delete_cookie("my_first_cookie")
driver.add_cookie({"name": "my_first_cookie", "value": "25"})
new_cookie = driver.get_cookie("my_first_cookie")

# Проверь новое значение поля value для добавленной куки
assert new_cookie["value"] == "25"

driver.quit()
