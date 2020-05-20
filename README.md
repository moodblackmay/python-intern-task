Установка:
1. git clone https://github.com/moodblackmay/python-intern-task.git
2. cd python-intern-task/
3. docker-compose up
4. Ctrl+C
5. docker-compose run web python manage.py migrate
6. docker-compose up
7. перейдите по http://0.0.0.0:8000/
8. вставьте guid компании в форму.


Например:


Если ссылка компании https://fedresurs.ru/company/ca48285e-8e7c-43d0-aced-798b759c5949


То ее guid=ca48285e-8e7c-43d0-aced-798b759c5949


Если среди сообщений есть упоминания о банкротстве то сервер выдаст guid задания.

Перейдите по http://0.0.0.0:8000/guid/<guid_задания>, чтобы посмотреть всю информацию о таких сообщениях.


Например: http://0.0.0.0:8000/guid/9e8173f6-829f-4a05-bb49-830bba2b669e


Данный сервис работает только с юридическими компаниями
