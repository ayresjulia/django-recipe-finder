# Python/Django recipe finder

![homepage_gif](./recipes/static/recipes/homepage.gif)

## :bulb: Description

FullStack Application made with Python/Django/PostgreSQL on backend and HTML/CSS/Jinja/Bootstrap on frontend, which allows user to fill out a form, include food allergies and view recipes that do not contain their allergens.

## :book: Features

- user is able to fill out a form and specify their food allergies

- backend logic filters out recipes from general recipe list according to allergens specified
  
- admin is able to modify user information and view which allergies they have and which recipes they can use (which do not contain user's allergens)
  
- user information is stored in the PostgreSQL database along with allergens and filtered recipes after form submission

## :pencil: Installation

- clone repository using command line

```terminal
$git clone https://github.com/ayresjulia/django-recipes.git
```

- create virtual environment and activate it

```terminal
$python3 -m venv venv
$source venv/bin/activate
```

- install all requirements

```terminal
$pip3 install -r requirements.txt
```

- run the app (NOTE: this app uses SECRET KEY that has been hidden, so app won't run unless you have it. please reach out to j.bobrineva@gmail.com for more details )

```terminal
$cd tinyorganics
$python3 manage.py runserver
```

- run tests

```terminal
$python3 manage.py test
```

## :key: API used

[Mock API for recipes](https://60f5adf918254c00176dffc8.mockapi.io/api/v1/recipes/)
[Mock API for BIG-8 allergens](https://60f5adf918254c00176dffc8.mockapi.io/api/v1/allergens/)

## :computer: Tech Stack

- Backend: Python/Django/PostreSQL
  
- Frontend: HTML/CSS/Jinja
  
- Libraries/modules: Bootstrap | django-crispy-forms

- Testing: django.test TestCase unittesting

## :battery: Work Process - strengths

- This app was my first app using Django, I had to learn it, and it was a blast! Django is more opinionated in comparison to Flask, however apps can be written faster with all available helpful features Django has.
  
- Django provides a functional admin page to easily see created models and modify existing Customers for the app

- For database I firstly decided to use SQLite while learning Django, as suggested in their docs. However, I made a switch to PostgreSQL database after my research has shown that deploying SQLite application would lose my database data at least one in 24 hours with cloud providers such as Heroku, AWS etc. PostgreSQL is one of most popular and powerful open source RDBMS, which follows SQL standards closely. PostgreSQL makes it easy to work with multi-relational tables and it is also more scalable.

- The biggest takeaway from this assessment, is that I learned how to make an app with Django and PostgreSQL, Django and SQLite, the differences between both databases, Django ease of use and framework's additional features (like admin page).
  
## :microscope: Work Process - opportunities/features to add

- User signup/login/logout feature

- Allow users to type in allergies instead of choosing among BIG-8, and use larger recipe API

- Create Recipe model assuming recipe API would be larger, and store not only recipe names but ingredients, allergens, descriptions etc

- Add stronger frontend, include animations and more exciting UI

- Include more tests depending on future features
