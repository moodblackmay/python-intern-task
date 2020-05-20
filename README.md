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


Данный сервис работает только с юридическими компаниями
