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

# change settings.py
$ pip install python-dotenv

# the write code
from dotenv import load_dotenv

load_dotenv()
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}
...


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

# create api directori and start write code

# create superuser for testing request
$ python3 manage.py createsuperuser
```

### Install and set up CORS
```
# Install CORS
$ python -m pip install django-cors-headers

# Change settings.py
INSTALLED_APPS = [
    ...,
    "corsheaders",
    ...,
]
and
MIDDLEWARE = [
    ...
    "corsheaders.middleware.CorsMiddleware",
    ...
]
and
CORS_ALLOWED_ORIGINS = True

and
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]
```

### Create taskcollection
```
$ python3 manage.py startapp taskcollection

# Add auth check
# on setting.py add 
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

# on taskcollection/views.py add
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
...
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_collections(request):

# and get data from access token on handler
@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def put_tasks(request):
    user = request.user
    return Response({"message": user.id})
```