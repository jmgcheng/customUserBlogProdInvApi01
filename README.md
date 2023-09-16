# Python - Django - Basic User Registration/Authentication, Blog, Product, Inventory, and API.

Python 3.11.0
pip 22.3 

In requirements.txt
```
pip freeze > requirements
pip install -r requirements.txt
```
asgiref==3.7.2
beautifulsoup4==4.12.2
crispy-bootstrap4==2022.1
Django==4.2.5
django-crispy-forms==2.0
html-sanitizer==2.2.0
lxml==4.9.3
Pillow==10.0.0
soupsieve==2.5
sqlparse==0.4.4
tzdata==2023.3



## Setup - Step 1

Go to desktop
```
cd desktop
```

Create project folder
desktop
```
mkdir projName01
```

Go in your project folder
desktop
```
cd projName01
```

Create environment named venv
desktop/projName01
```
python -m venv venv
```

Activate environment
desktop/projName01
```
venv\Scripts\activate.bat
```

Install django
(venv) desktop/projName01
```
python -m pip install Django
```

Start project
(venv) desktop/projName01
```
django-admin startproject core
```

cd in your project
(venv) desktop/projName01
```
cd core
```

IDE
- drag outer core folder in your IDE(visual studio code)
OR
(venv) desktop/projName01/core
```
code .
```

## Setup - Step 2

1. Create app pages, users, posts, files, products, purchases, sales
```python
python manage.py startapp pages
python manage.py startapp users
python manage.py startapp posts
python manage.py startapp files
python manage.py startapp products
python manage.py startapp purchases
python manage.py startapp sales
pip install django-crispy-forms
pip install crispy-bootstrap4
pip install pillow
pip install html-sanitizer
```

2. Static and Templates. [Bootstrap4 Starter Template](https://getbootstrap.com/docs/4.0/getting-started/introduction/#starter-template) 
```
> projName01
    > media
    > media_cdn
	> static
		> main.css
	> templates
		> base.html
    > pages/users/posts/files/products/purchases/sales
        > templates
            > pages/users/posts/files/products/purchases/sales
                > .html
```

3. setup settings.py

4. setup views.py for pages, users, posts, files, products, purchases, sales

5. setup models.py for users, posts, files, products, purchases, sales

6. setup forms.py for users, products, purchases, sales

7. setup admin.py for users, posts, files, products, purchases, sales

8. setup mixins.py for posts, files, products, purchases, sales

9. setup urls.py for core, pages, users, posts, files, products, purchases, sales

10. Migrations, Super user, Run server
```python
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

11. Create Data
- go to admin and create dummy Products, Colors, Sizes, Units before using the frontend
- product url best for 300x300 for now
