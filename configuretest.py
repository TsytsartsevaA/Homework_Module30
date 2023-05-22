from settings import valid_email, valid_password
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest


driver = webdriver.Chrome(executable_path="C:\Users\sysma\PycharmProjects\Homework_Module30/chromedriver.exe")

@pytest.fixture(autouse=True, scope="session")
def testing():
    pytest.driver = webdriver.Chrome('C:\Users\sysma\PycharmProjects\Homework_Module30/chromedriver.exe')

    # активируем неявное ожидание (время браузеру на загрузку страницы)
    pytest.driver.implicitly_wait(5)

    # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends.skillfactory.ru/login')

    # Очищаем поле для ввода email и вводим email
    field_email = pytest.driver.find_element(By.ID, 'email')
    field_email.clear()
    field_email.send_keys(valid_email)

    # Очищаем поле для ввода пароля и вводим пароль
    field_pass = pytest.driver.find_element(By.ID, 'pass')
    field_pass.clear()
    field_pass.send_keys(valid_password)
    time.sleep(2)

    # Нажимаем кнопку входа в аккаунт
    pytest.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Проверяем нахождение на главной странице пользователя
#    assert pytest.driver.current_url == 'https://petfriends.skillfactory.ru/all_pets', "Некорректный email или пароль"
    if not pytest.driver.current_url == 'https://petfriends.skillfactory.ru/all_pets':
        pytest.driver.quit()
        raise Exception("Некорректный email или пароль")

    # ЕСЛИ ОКНО БРАУЗЕРА не "НА ВЕСЬ ЭКРАН", то надо нажать на иконку
    if pytest.driver.find_element(By.XPATH, "//body/nav[1]/button[1]").is_displayed():
        time.sleep(2)
        pytest.driver.find_element(By.XPATH, "//body/nav[1]/button[1]").click()
        time.sleep(2)

    # Нажимаем на ссылку "Мои питомцы"
    pytest.driver.find_element(By.XPATH, "//a[contains(text(),'Мои питомцы')]").click()

    # Проверяем переход на страницу "Мои питомцы"
#    assert pytest.driver.current_url == 'https://petfriends.skillfactory.ru/my_pets', "Это не страница "Мои питомцы""
    if not pytest.driver.current_url == 'https://petfriends.skillfactory.ru/my_pets':
        pytest.driver.quit()
        raise Exception('Это не страница "Мои питомцы"')

    yield

    pytest.driver.quit()