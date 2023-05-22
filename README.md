# Homework_Module30
Написан тест, проверяющий, что на странице https://petfriends.skillfactory.ru/my_pets со списком питомцев пользователя:

1. Присутствуют все питомцы.
2. Хотя бы у половины питомцев есть фото.
3. У всех питомцев есть имя, возраст и порода.
4. У всех питомцев разные имена.
5. В списке нет повторяющихся питомцев.
6. В написанном тесте (проверка карточек питомцев) надо добавить неявные ожидания всех элементов (фото, имя питомца, его возраст).
7. В написанном тесте (проверка таблицы питомцев) надо добавить явные ожидания элементов страницы Файл settings.py - верные email и пароль.

# Запуск тестов:
# pytest -v -s -q --driver Chrome --driver-path <путь>/chromedriver.exe test_pets_friends.py
# pytest -v -s -q --driver Chrome --driver-path C:\Users\sysma\PycharmProjects\Homework_Module30\chromedriver.exe test_pets_friends.py
