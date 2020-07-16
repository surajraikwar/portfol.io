# KnowMe

A platform to showcase all your projects at a single place with changeable themes.

The live version can be found [here](surajraikwar.herokuapp.com)

## Running on local machine

- pull repository to local machine

- setup database

install required packages

```
   sudo apt-get update
   sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib
```

create database `knowme`

```
    sudo su - postgres
    psql
    CREATE DATABASE knowme;
    CREATE USER suraj WITH PASSWORD 'password';
    GRANT ALL PRIVILEGES ON DATABASE knowme TO suraj;
```

- install WKHTMLTOPDF packages

```
    sudo apt update
    sudo apt -y install wget
    wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.bionic_amd64.deb
    sudo apt install ./wkhtmltox_0.12.5-1.bionic_amd64.deb
```

- create and activate virtual environment

```
    pip install virtualenv
    virtualenv myenv
    source myenv/bin/activate
```

- install requirements

```
    cd knowme
    pip install -r requirements.txt
```

- start project on local server

```
    python manage.py runserver
```

- now go to [127.0.0.1:8000](127.0.0.1:8000)
