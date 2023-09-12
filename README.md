# yatube

Cтек технологий
----------
* Python 3.7
* Django 2.2
* SQLite3
* CSS
* JS
* HTML

Запуск проекта локально
----------
1. Клонировать репозиторий и перейти в него в командной строке:
```
git@github.com:GlebMudrov/yatube.git

cd yatube
```
2. Cоздать и активировать виртуальное окружение:
```
py -3.7 -m venv venv

. venv/Scripts/activate
```
3. Установить зависимости:
```
python -m pip install --upgrade pip

pip install -r requirements.txt
```
4. Выполнить миграции:
```
cd yatube

python3 manage.py migrate
```
5. Создать суперпользователя:
```
python manage.py сreatesuperuser
```
6. Запустить проект:
```
python manage.py runserver
```

### Автор проекта:  <a href= "https://github.com/GlebMudrov">__Мудров Глеб__<a/>