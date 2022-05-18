
# This project is to technical interview of Flat.mx


## Overview:

API Rest to get data from a repository, in this case we are going to retrive: Authors, Commits, Branches and Pull Request, using [GitHub Rst API v3](https://docs.github.com/en/rest)


To see a full list of the API methods and endpoints please refere to the API Documentation [here](https://github.com/RoodrigoRoot/flat-backend-test/blob/main/docs/api_documentation.md).

Get .env file with values [here](https://drive.google.com/file/d/1jOlbgr-zkTpOy-xwOeUQZTl3q8varKy0/view?usp=sharing)
##### **This file only for 7 days and after taht it will be deleted**
##### **Only put this file in the root**

## Objectives

This project proposes a solution based on Api Rest based on this interview [Flat Digital Backend Interview](https://github.com/FlatDigital/backend-gitwrap-test)


## Use cases to support:

- Anyone can use this project

- Create an API REST to:

- Create Pull Request

- Merge Pull Request

- Get all Pull Request

- Get details Pull Request

- Get all commits repository

- Get details commit

- Get all branches repository

- Get all authors repository


## Use cases unsupported:

- Login for users

- Create users

- Save Commits on DB

- Save Branches on DB

- Delete Branches

- Delete Commits

- Delete Pull Request


## Stack's technology

- Python

- Django

- PostgreSQL

- Docker

- Docker Compose

- Makefile


## The structure this project is based on:

[Django StyleGuide from HackSoftware](https://github.com/HackSoftware/Django-Styleguide)

**with some changes**


## Instructions

#### These instructions use [make](https://es.wikipedia.org/wiki/Make) to streamline interaction with the project.

> Note: If not had `make` on your compute at the bottom of this page are instructions with docker commands


### To build and run project

**Build project**

`make build`


**Run project**

`make run`


#### To stop project

`make stop`


## Other commands

#### To enter the inside of the container bash

`make bash`


#### To watch logs of Back

`make logs-back`


#### To watch logs of DB

`make logs-db`


## Instructions with Docker Compose

#### To run project

`docker-compose up`


#### To stop project

`docker-compose stop`


## Documentation

For this project we use Swagger and postman

[Collection of Postman](https://drive.google.com/file/d/1lCvnCTeXM9iQMwOxkzadjMJ6ULd1UDne/view?usp=sharing)

With swagger we need run the project and go to '/api/v1/docs/'
[Swagger](http://localhost:8000/api/v1/docs/)
