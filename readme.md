# Diplom Work Chitai-Gorod

## Описание проекта

Этот проект предназначен для автоматизации тестирования веб-сайта "Читай-город" с использованием Selenium для UI тестов и `requests` для API тестов. Проект включает тесты для поиска книг, добавления книг в корзину, изменения количества книг в корзине и удаления книг из корзины.

## Ссылка на проект
https://nuiunion.yonote.ru/share/895aa283-18d2-432d-bb83-ea96c94c07ce

## Структура проекта

- `api_data/`
  - `cart_api.py`: Содержит класс `CartApi` для взаимодействия с API корзины.
- `ui_data/`
  - `search_ui.py`: Содержит класс `SearchUI` для взаимодействия с UI поиска.
- `test/`
  - `conftest.py`: Содержит фикстуры для настройки браузера и базовых URL.
  - `test_api.py`: Содержит тесты для API корзины.
  - `test_ui.py`: Содержит тесты для UI поиска.

## Установка

1. Клонируйте репозиторий:
   git clone https://github.com/yourusername/diplom_work_chitai.git
   cd diplom_work_chitai

## Установите зависимости
pip install -r requirements.txt

## Запуск тестов

Для запуска UI тестов используйте команду:
pytest test/test_ui.py --alluredir=allure-results

Для запуска API тестов используйте команду:
pytest test/test_api.py --alluredir=allure-results

## Просмотр отчётов Allure

Установите Allure:

Инструкция по установке Allure - https://allurereport.org/docs/#_installing_a_commandline
Сгенерируйте и откройте отчёт:
allure serve allure-results
