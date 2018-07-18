# REFUGEE SYSTEM

This is a refugee management system built using django

  - Python3
  - Django 2.0+
  -Sqlite

# Installation
To run the development version :

  - clone this repo
  - navigate into the root folder
  - run the following in terminal
   ```sh
$ pip install -r requirements.txt
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py collectstatic
$ python3 manage.py createsuperuser
```

-Finally run
```sh
$   python3 manage.py runserver
```
Visit the site on your browser at [localhost:8000/](http://localhost:8000/)
