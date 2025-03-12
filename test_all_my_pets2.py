# start:  python -m pytest -v --driver Chrome --driver-path C:\PyCharm\Projects\Testing\chromedriver.exe test_all_my_pets2.py
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()
    # Переходим на страницу авторизации
    driver.get('https://petfriends.skillfactory.ru/login')
    driver.set_window_size(1920, 1080)
    driver.implicitly_wait(8)

    yield driver

    driver.quit()


def test_show_all_pets(driver):
    # Вводим email
    driver.find_element(By.ID, 'email').send_keys('kseniya2312@gmail.com')
    # Вводим пароль
    time.sleep(1)
    driver.find_element(By.ID, 'pass').send_keys('9992175077Zx')
    time.sleep(1)
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    time.sleep(2)

    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    images = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
    names = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
    descriptions = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0


def test_show_my_pets(driver):

    driver.find_element(By.ID, 'email').send_keys('kseniya2312@gmail.com')

    driver.find_element(By.ID, 'pass').send_keys('9992175077Zx')

    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul[1]/a[1]').click()
    assert driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul[1]/a').text == "Мои питомцы"

    driver.implicitly_wait(8)
    driver.find_element(By.XPATH, '//table[@class="table table-hover"]/tbody/tr')

    images = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
    names = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
    descriptions = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0