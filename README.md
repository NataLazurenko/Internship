## Интерактивная платформа-сообщество для стажеров и участников молодежных карьерных проектов
Наша реализация платформы использует фреймворк Django для своего бэкенда и фронтенда. Для тестирования все данные хранятся в sqlite3-базе данных, в дальнейшем
планируется использование PostgreSQL, весь сайт написан с использованием протитипных CSS стилей.

## Локальная сборка проекта
Клонируем проект с github
```bash
git clone https://github.com/NataLazurenko/Internship.git
```
Создаём виртуальное окружение Python и активируем его
 ```bash
 python3 -m venv env
 source evn/bin/activate
 ```
 Ставим необходимые зависимости для проекта
 ```bash
 pip3 install -r requirements.txt
 ```
 Запускаем сервер
 ```bash
 python3 manage.py runserver
 ```
