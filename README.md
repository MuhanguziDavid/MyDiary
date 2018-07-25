# MyDiary
[![Build Status](https://travis-ci.com/MuhanguziDavid/MyDiary.svg?branch=develop)](https://travis-ci.com/MuhanguziDavid/MyDiary)
[![Coverage Status](https://coveralls.io/repos/github/MuhanguziDavid/MyDiary/badge.svg?branch=develop)](https://coveralls.io/github/MuhanguziDavid/MyDiary?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/c48c9fc84c9e037b3304/maintainability)](https://codeclimate.com/github/MuhanguziDavid/MyDiary/maintainability)

MyDiary is an online journal that provides users with the ability to pen down their thoughts and feelings

## Features
MyDiary offers the following features
* Create an account and login
* View all entries in a diary
* View contents of a diary entry
* Add an entry
* Modify an entry
* Set and get notifications to add an entry to the diary

Visit the site:
https://muhanguzidavid.github.io/MyDiary/UI/index.html

## Getting Started

### Prerequisites
* Python 3
* python-pip

###Installation
* Clone the project at [MyDiary](https://github.com/MuhanguziDavid/MyDiary).
* cd into the project diractory
* Set up a virtual environment and activate it
* Install all dependencies (pip install -r requirements.txt)

### Running the app
* Run the app with the command (python run.py)
* Open postman and run (http://127.0.0.1/5000/api/v1/entries)

### Supported endpoints
HTTP Method | Endpoint | Description
------------ | ------------- | -------------
GET| /api/v1/entries| Retrieves all diary entries
GET| /api/v1/entry/<int:entry_id>| Retrieves a specific diary entry
POST| /api/v1/entry/<int:entry_id>| Adds an entry to the diary
PUT| /api/v1/entry/<int:entry_id>| Updates an entry in the diary
DELETE| /api/v1/entry/<int:entry_id>| Deletes an entry from the diary

### Tests

To run tests, run the command (pytest -v)

###Deployment

The application has been deployed on heroku: https://my-diary-entries.herokuapp.com/api/v1/entries
