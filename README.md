# Run server
```
$ python3 manage.py runserver
```

## Dependencies
```
# Create requirements.txt
$ pip freeze > requirements.txt

# Install requirements
$ pip install -r requirements.txt
```

### Install wsl and python
```
# After instaled wls instal python
$ sudo apt update && upgrade
$ sudo apt install python3 python3-pip ipython3

# Install venv
$ sudo apt install python3-venv

# Install django
$ sudo apt get python3-django
```

### Create django project
```
# Create project
$ django-admin startproject moderntodo

# Create auth app on moderntodo directori
$ python3 manage.py startapp authapp

# After create django app you need add this app to INSTALLED_APPS on setting.py 
```

### Create virtual environment like best practic
```
$ python3 -m venv .vend

# If use wsl
$ source .venv/bin/activate
```

### UP DB on docker
```
# Create docker network
$ docker network create moderntodo-network

# Run docker container with DB
$ docker run --name modernToDo --network moderntodo-network -p 5433:5432 -e POSTGRES_USER=root -e POSTGRES_PASSWORD=secret -d postgres

# Connect to DB
$ docker exec -it modernToDo psql -U root

# Create DB
# connect to postgres on docker
$ docker exec -it modernToDo psql -U root
# create DB
$ CREATE DATABSE modernToDoDB;



# POSTGRES CLI

# If you want to check DB
$ \l
# For check table on DB
# go to the DB
$ \c moderntododb
# Check table
$ \dt
# check area on table
$ SELECT * FROM [table name]

``` 

### Make auth
```
# Install djangorestframework and djangorestframework_simplejwt
$ pip install djangorestframework djangorestframework-simplejwt

# After this add to installed app on settings.py 
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework_simplejwt',
    ...
]

# and set up JWT
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}
```