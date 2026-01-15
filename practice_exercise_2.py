import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://qa-mesto.praktikum-services.ru/")

# Выполни авторизацию
driver.find_element(By.ID, "email").send_keys("alexandr_29@gmail.com")
driver.find_element(By.ID, "password").send_keys("123456qA")
driver.find_element(By.CLASS_NAME, "auth-form__button").click()

# Добавь явное ожидание загрузки страницы
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "places__list")))

# Запомни title последней карточки
cart_list = driver.find_elements(By.XPATH, "//li[@class='places__item card']")
title_before = cart_list[0].find_element(By.TAG_NAME, "h2").text

# Кликни по кнопке добавления нового контента
driver.find_element(By.CLASS_NAME, "profile__add-button").click()

# сгенерируй новое место и введи его в поле названия
new_title = "Москва" + str(random.randint(100, 999))
driver.find_element(By.ID, "place-name").send_keys(new_title)

# В поле ссылки на изображение введи ссылку
driver.find_element(By.ID, "place-link").send_keys("https://code.s3.yandex.net/qa-automation-engineer/python/files/photoSelenium.jpeg")

# Сохрани контент
driver.find_element(By.XPATH, ".//form[@name='new-card']//button[text()='Сохранить']").click()

# Дождись появления кнопки удаления карточки
button_delete_xpath = f".//h2[text()='{new_title}']//ancestor::li//button[@class='card__delete-button card__delete-button_visible']"
WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, button_delete_xpath)))

# Проверь, что на карточке отображается верное название
title_after = driver.find_element(By.XPATH, f".//h2[text()='{new_title}']").text
assert new_title == title_after

# Запомни количество карточек до удаления
cards_before = len(driver.find_elements(By.XPATH, "//li[@class='places__item card']"))

# Удали карточку
driver.find_element(By.XPATH, button_delete_xpath).click()

# Дождись, что title последней карточки равен title_before
WebDriverWait(driver, 3).until(expected_conditions.text_to_be_present_in_element(
    (By.XPATH, "//li[@class='places__item card']//h2[@class='card__title']"), title_before))

# Проверь, что количество карточек стало на одну меньше
cards_after = len(driver.find_elements(By.XPATH, "//li[@class='places__item card']"))
assert cards_before - cards_after == 1

driver.quit()
