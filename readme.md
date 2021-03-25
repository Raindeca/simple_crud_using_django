# Point of Sale Application
## _XYZ Bookstore - BNSP Programming_

![N|Solid](https://cdn.discordapp.com/attachments/769771830894395425/824431764725432320/unknown.png)


This Application was created in order to answer XYZ Boostore problem regarding **Point of Sale**. This web-based application is used **Django** as it's main framework and could perform simple *Create, Read, Update, Delete (CRUD)* for each main object defined.

**Badan Nasional Sertifikasi Profesi (BNSP**) is an independent institution from the government that aims to provide professional certification to all people in Indonesia. This application was created in order to fulfilled the competency requirement on that institution.


## Features
This application has several Features, there are:
- Using CRUD Concept for storing data
- Url was created by using REST API convention structure
- Interactive table design
- HTML was created in jinja2 for better performance

##  Prerequisites
- Django **v3.1.7**
- Python **v3.7.7**
- Pip **v19.2.3**
 

## Setup
Ensure you have cloned/pulled the repository to your local. Open terminal in the root repository and run all these commands.

1. Create virtual local python environment
    ```sh
    python -m venv env
    ```

2.  Activate local environment we just created.
    ```sh
    env\Scripts\activate.bat
    ```

3.  Install Django
    ```sh
    pip install django
    ```

## Usage
* ### Run application
    Before you follow these instructions, ensure that you already **activated local environment**. After that, here are things you need to do..
    1. Run the application
        ```sh
        python manage.py runserver
        ```
* ### Migrate a model
    Assume you already started the application. Here are available commands you could use on this project:
    - Make migrations if you edit/create a model
        ```sh
        python manage.py makemigrations
        ```
    - Migrate
        ```sh
        python manage.py migrate
        ```
* ### Create a superuser
    Create superuser in order to use admin pannel in django, here are the steps for creating it:

    - Ensure you already started the application before do these steps:
        ```sh
        python manage.py createsuperuser
        ```
    - Access the admin pannel of django using this url:
        ```sh
        http://127.0.0.1:8000/admin/
        ```
## Documentation
Use these urls below to access each section in the application:
    1. Accessing Book List:
    ```
        http://127.0.0.1:8000/book/
    ```
    2. Accessing Costumer List:
    ```
        http://127.0.0.1:8000/costumer/
    ```
    3. Accessing Transactionr List:
    ```
        http://127.0.0.1:8000/transaction/
    ```

See more details on ``urls.py`` in each application folder in this app.

## Maintainers
- [Raindeca Dzulikrom Haqqu](https://github.com/Raindeca/)

## Acknowledgements
- Badan Nasional Sertifikasi Profesi
- Gunadarma University
- Django, python, and all libraries
