# File Service Web Application

[](https://github.com/omar-bendary/restaurant-task/tree/main#restaurant-reservation-api)

# Features

* **File Upload** : Upload a text file and store it.
* **Random Line** : Return a random line from an uploaded file in different formats (text, JSON, XML).
* **Random Line Backwards** : Return a random line from an uploaded file, reversed.
* **Longest 100 Lines** : Return the 100 longest lines across all uploaded files.
* **Longest 20 Lines of One File** : Return the 20 longest lines from a specific uploaded file.

# Getting started

[](https://github.com/omar-bendary/restaurant-task/tree/main#getting-started)

## Installation

[](https://github.com/omar-bendary/restaurant-task/tree/main#installation)

make a new folder for the project and open this folder in the Terminal/Windows (PowerShell) and run this command

```shell
git clone https://github.com/omar-bendary/file_uploader
```

# Pre-requisites and Local Development

[](https://github.com/omar-bendary/restaurant-task/tree/main#pre-requisites-and-local-development)

# Using Docker and Docker compose

[](https://github.com/omar-bendary/restaurant-task/tree/main#using-docker-and-docker-compose)

The first step is to sign up for a free account on [DockerHub](https://hub.docker.com/signup) and then install the Docker desktop app on your local machine:

* [Docker for Mac](https://docs.docker.com/desktop/install/mac-install/)
* [Docker for Windows](https://docs.docker.com/desktop/install/windows-install/) Once Docker is done installing we can confirm the correct version is running by typing the command docker --version in the command line shell

```shell
$ docker --version
Docker version 20.10.14, build a224086
```

### Running our container

[](https://github.com/omar-bendary/restaurant-task/tree/main#running-our-container)

1- Open the project Code folder in Terminal/Windows (PowerShell).

2- Run this command .

```shell
docker-compose up -d --build
```

### To Stop the currently running container

[](https://github.com/omar-bendary/restaurant-task/tree/main#to-stop-the-currently-running-container)

Control+c (press the “Control” and “c” button at the same time) and additionally type docker-compose down.

```shell
docker-compose down
```

### Now let’s confirm everything is working

[](https://github.com/omar-bendary/restaurant-task/tree/main#now-lets-confirm-everything-is-working)

```shell
docker-compose exec web python manage.py  makemigrations 
```

```shell
docker-compose exec web python manage.py  migrate 
```

> Now create the admin user

```shell
 docker-compose exec web python manage.py createsuperuser 
```

The application is run on [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### Set up your RDBMS , open your setting.py

[](https://github.com/omar-bendary/restaurant-task/tree/main#set-up-your-rdbms--open-your-settingpy)

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "db",  # set in docker-compose.yml
        "PORT": 5432,  # default postgres port
    }
}
```

All the extracted data is saved to the database to use it later if needed.

# Using virtual environment approach.

[](https://github.com/omar-bendary/restaurant-task/tree/main#using-virtual-environment-approach)

## To create a virtual environment

[](https://github.com/omar-bendary/restaurant-task/tree/main#to-create-a-virtual-environment)

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install packages.

1- Open the project Code folder in Terminal/Windows (PowerShell).

2- Run this command .

```shell
# Windows
> python -m venv .venv
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# macOS
% python3 -m venv .venv
```

### To activate a new virtual environment called .venv:

[](https://github.com/omar-bendary/restaurant-task/tree/main#to-activate-a-new-virtual-environment-called-venv)

```shell
# Windows
> .venv\Scripts\Activate.ps1
(.venv) >

# macOS
% source .venv/bin/activate
(.venv) %
```

### To deactivate and leave a virtual environment type deactivate.

[](https://github.com/omar-bendary/restaurant-task/tree/main#to-deactivate-and-leave-a-virtual-environment-type-deactivate)

```shell
# Windows
(.venv) > deactivate
>

# macOS
(.venv) % deactivate
%
```

### install requirements.txt

[](https://github.com/omar-bendary/restaurant-task/tree/main#install-requirementstxt)

Run `pip install requirements.txt`. All required packages are included in the requirements file.

> make sure to activate the virtual environment first

```shell
pip install -r requirements.txt
```

**You might see a WARNING message about updating pip after running these commands. It’s always good to be on the latest version of software and to remove the annoying WARNING message each time you use pip. You can either copy and paste the recommended command or run `python -m pip install --upgrade pip` to be on the latest version.**

```shell
(.venv) > python -m pip install --upgrade pip
```

## Now let’s confirm everything is working by running Django’s internal web server via the runserver command

[](https://github.com/omar-bendary/restaurant-task/tree/main#now-lets-confirm-everything-is-working-by-running-djangos-internal-web-server-via-the-runserver-command)

```shell
(.venv) > python manage.py  makemigrations 
```

```shell
(.venv) > python manage.py  migrate 
```

> Now create the admin user

```shell
(.venv) > python manage.py createsuperuser 
```

Run the surver

```shell
# Windows
(.venv) > python manage.py runserver

# macOS
(.venv) % python3 manage.py runserver
```

## Set up your RDBMS , open your setting.py

[](https://github.com/omar-bendary/restaurant-task/tree/main#set-up-your-rdbms--open-your-settingpy-1)

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_project_name',
        'USER': 'your_postgres_username',
        'PASSWORD': 'your_postgres_password',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '5432',
    }
}
```

Or you can stick the default database (sqlite3) but not recommended for Production.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

All the extracted data is saved to the database to use it later if needed.
The application is run on [http://127.0.0.1:8000/api](http://127.0.0.1:8000/api) by default in the backend configuration.

# API Documentation

You can acess Swagger UI or ReDoc interface

* `/swagger/`: Provides a Swagger UI interface for interacting with your API.
* `/redoc/`: Provides a ReDoc interface for your API documentatio

#### Endpoints

1. **Upload a File** :

* **URL** : `/api/files/upload/`
* **Method** : `POST`
* **Request** :
  * `file`: The text file to upload
* **Respnse**

```json
{
    "id": 1,
    "file": "uploads/filename.txt",
    "uploaded_at": "2024-07-07T12:34:56.789Z"
}

```

2. **Get a Random Line** :

* **URL** : `/api/files/{file_id}/random_line/`
* **Method** : `GET`
* **Response** (`application/json`):

  ```json
  {
      "line_number": 4,
      "file_name": "uploads/filename.txt",
      "line": "This is a random line from the file.",
      "most_common_letter": "e"
  }

  ```

3. **Get a Random Line Backwards** :

* **URL** : `/api/files/{file_id}/random_line_backwards/`
* **Method** : `GET`
* **Response** :
  ```plaintext
  .elif eht morf enil modnar a si sihT
  ```

4. **Get the 100 Longest Lines Across All Files** :

* **URL** : `/api/files/longest_100_lines/`
* **Method** : `GET`
* **Response** :

  ```json
  [
      "This is the longest line in the file.",
      "This is the second longest line in the file.",
      ...
  ]

  ```

5. **Get the 20 Longest Lines of One File** :

* **URL** : `/api/files/{file_id}/longest_20_lines/`
* **Method** : `GET`
* **Response** :

```json
[
    "This is the longest line in the file.",
    "This is the second longest line in the file.",
    ...
]

```
