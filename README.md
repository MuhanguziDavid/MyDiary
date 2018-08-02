# MyDiary
[![Build Status](https://travis-ci.com/MuhanguziDavid/MyDiary.svg?branch=challenge-3)](https://travis-ci.com/MuhanguziDavid/MyDiary)
[![Coverage Status](https://coveralls.io/repos/github/MuhanguziDavid/MyDiary/badge.svg?branch=challenge-3)](https://coveralls.io/github/MuhanguziDavid/MyDiary?branch=challenge-3)
[![Maintainability](https://api.codeclimate.com/v1/badges/c48c9fc84c9e037b3304/maintainability)](https://codeclimate.com/github/MuhanguziDavid/MyDiary/maintainability)

MyDiary is an online journal that provides users with the ability to pen down their thoughts and feelings

## Features
MyDiary offers the following features
* Create an account for a user
* Login a user
* View all entries in a user's diary
* View contents of a diary entry
* Add an entry
* Modify an entry
* Delete an entry

Visit the site:
https://muhanguzidavid.github.io/MyDiary/UI/index.html

## Getting Started

### Prerequisites
```
Python 3
python-pip
Virtualenv
```

### Installation

* Clone the project at [MyDiary](https://github.com/MuhanguziDavid/MyDiary).
* cd into the project diractory

#### Setup Virtual environment
For windows:
```
virtualenv env
cd/env/scripts/activate
```

#### Install all dependencies
```
 pip install -r requirements.txt
```

#### Setting up the database
* Install postgresql 10
* In the terminal, enter the following command to shift to the postgres shell
```
psql -U <username> postgres
```
* In postgress shell, create mydiary database
```
CREATE DATABASE mydiary;
```

### Running the app
* Run the app with the command (python run.py)
* Open postman and run (http://127.0.0.1/5000/api/v1/entries)

## Supported endpoints
HTTP Method | Endpoint | Description
------------ | ------------- | -------------
POST| /api/v1/auth/signup| Registers a user
POST| /api/v1/auth/login| Login a user
GET| /api/v1/entries| Retrieves all diary entries
GET| /api/v1/entry/<int:entry_id>| Retrieves a specific diary entry
POST| /api/v1/add| Adds an entry to the diary
PUT| /api/v1/update| Updates an entry in the diary
DELETE| /api/v1/remove/<int:entry_id>| Deletes an entry from the diary

## Tests

To run tests, run the command (pytest -v)

* cd into the tests folder
* run the command 
```
pytest -v test_diary.py
```

### Tests with coverage
Run the command
```
nosetests --with-coverage --cover-tests --cover-package=tests
```

## Deployment
The application has been deployed on heroku:
https://my-diary-3.herokuapp.com/api/v1/auth/signup
