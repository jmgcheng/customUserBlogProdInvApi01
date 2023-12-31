# Python - Django - Basic User Registration/Authentication, Blog, Product, Inventory, and API.

Python 3.11.0
pip 22.3 

In requirements.txt
```
pip freeze > requirements.txt
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



## Pylance Issue in Visual Code
1. View > Command Palette OR Ctrl+Shift+P
2. Python: Select Interpreter
3. + Enter interpreter path...
4. choose your project python.exe eg "venv\Scripts\python.exe"



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


## Setup - Step 3 - API Setup

1. Create app api and install django rest framework
```python
python manage.py startapp api
pip install djangorestframework
```

2. setup settings.py
```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework.authtoken',
    'api',
    ...
]
```

3. Migrate
```python
python manage.py makemigrations
python manage.py migrate
```

4. setup api/serializers.py

5. setup api/views.py

6. setup root urls.py
```python
urlpatterns = [
    ...
    path('api/', include('api.urls')),
    ...
]
```

7. setup api/urls.py
```python
from django.urls import path
from .views import PurchaseListCreateView, PurchaseRetrieveUpdateDestroyView, SaleListCreateView, SaleRetrieveUpdateDestroyView, ProductVariationListCreateView, ProductVariationRetrieveUpdateDestroyView
from rest_framework.authtoken import views


urlpatterns = [
    path('purchases/', PurchaseListCreateView.as_view()),
    path('purchases/<int:pk>/', PurchaseRetrieveUpdateDestroyView.as_view()),

    path('sales/', SaleListCreateView.as_view()),
    path('sales/<int:pk>/', SaleRetrieveUpdateDestroyView.as_view()),

    path('products/', ProductVariationListCreateView.as_view()),
    path('products/<int:pk>/', ProductVariationRetrieveUpdateDestroyView.as_view()),

    path('api-token-auth/', views.obtain_auth_token),
]
```

8. go to admin and generate a token for a user that will test the api in Postman if authentication is applied in views.py

9. get token in api using Postman
```
POST
    http://localhost:8000/api/api-token-auth/
BODY > x-www-form-urlencoded
    username
        admin@yahoo.com <- depends on your setup if username or email
    password
        1234
```

10. get list of products using Postman
```
GET
    http://127.0.0.1:8000/api/products/
Headers
    Authorization
        token theTokenThatYouGot
```

11. get specific product using Postman
```
GET
    http://127.0.0.1:8000/api/products/3/
Headers
    Authorization
        token theTokenThatYouGot
```

12. list purchases in Postman
```
GET
    http://127.0.0.1:8000/api/purchases/
Headers
    Authorization
        token theTokenThatYouGot
```

13. list sales in Postman
```
GET
    http://127.0.0.1:8000/api/sales/
Headers
    Authorization
        token theTokenThatYouGot
```

14. add purchases in Postman
```
POST
    http://127.0.0.1:8000/api/purchases/
Headers
    Authorization
        token theTokenThatYouGot
Body > raw > JSON
{
    "code": "PO0010",
    "purchase_detail": [
        {
            "product_variation": 1,
            "quantity_purchased": 50
        },
        {
            "product_variation": 2,
            "quantity_purchased": 50
        },
        {
            "product_variation": 3,
            "quantity_purchased": 50
        }
    ]
}
```

15. add sales in Postman
```
POST
    http://127.0.0.1:8000/api/sales/
Headers
    Authorization
        token theTokenThatYouGot
Body > raw > JSON
{
    "code": "SO0005",
    "sale_detail": [
        {
            "product_variation": 1,
            "quantity_purchased": 10
        },
        {
            "product_variation": 2,
            "quantity_purchased": 20
        }
    ]
}
```

16. get specific purchase in Postman
```
GET
    http://127.0.0.1:8000/api/purchases/1/
Headers
    Authorization
        token theTokenThatYouGot
```

17. get specific sale in Postman
```
GET
    http://127.0.0.1:8000/api/sales/1/
Headers
    Authorization
        token theTokenThatYouGot
```

18. update specific purchase in Postman
```
PUT
    http://127.0.0.1:8000/api/purchases/1/
Headers
    Authorization
        token theTokenThatYouGot
Body > raw > JSON
{
    "code": "PO0010",
    "purchase_detail": [
        {
            "product_variation": 1,
            "quantity_purchased": 50
        },
        {
            "product_variation": 2,
            "quantity_purchased": 50
        },
        {
            "product_variation": 3,
            "quantity_purchased": 50
        }
    ]
}
```

19. update specific purchase in Postman
```
PUT
    http://127.0.0.1:8000/api/sales/1/
Headers
    Authorization
        token theTokenThatYouGot
Body > raw > JSON
{
    "code": "SI0005",
    "sale_detail": [
        {
            "product_variation": 1,
            "quantity_released": 20
        }
    ]
}
```

20. DELETE specific purchase in Postman
```
DELETE
    http://127.0.0.1:8000/api/purchases/1/
Headers
    Authorization
        token theTokenThatYouGot
```

21. DELETE specific purchase in Postman
```
DELETE
    http://127.0.0.1:8000/api/sales/1/
Headers
    Authorization
        token theTokenThatYouGot
```


## Setup - Step 4 - API - CORS
1. Install django-cors-headers
```
pip install django-cors-headers
```

2. settings.py Setup below works on local BUT still unsure if same in live
```
INSTALLED_APPS = [
    ...
    'corsheaders',    
    ...
]

MIDDLEWARE = [
    ...
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
]

# Allow all origins in development; you may want to restrict this in production
CORS_ALLOW_ALL_ORIGINS = os.getenv('DJANGO_CORS_ALLOW_ALL_ORIGINS', default=False)

# List of allowed origins (comma-separated)
CORS_ALLOWED_ORIGINS = [
    "http://localhost:4200",  # Replace with the URL of your Angular app
    # Add other allowed origins here as needed
]

# Other CORS settings (optional)
CORS_ALLOW_METHODS = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS']
CORS_ALLOW_HEADERS = ['*', 'Authorization']
```

# Git clone setup
- it seems there's an issue when doing clone and using pip install -r requirements.txt
	- I need more trial installation next time to see what's best and log here
- what I did was git clone, then paste a venv and db.sqlite3 from a similar project
	- what's left was copy paste static media folders

# Amazon EC2 Cloud Terminal Setup
1. update ubuntu
```
sudo apt-get update
```

2. upgrade packages
```
sudo apt-get upgrade
```

3. check python version
```
python3 --version
```

4. clone repo
```
git clone https://github.com/jmgcheng/customUserBlogProdInvApi01.git
```

5. go in your project
```
cd customUserBlogProdInvApi01
```

6. install project requirements.txt
```
cd core
pip install -r requirements.txt
cd ..
```

7. install python virtual environment
```
sudo apt-get install python3-venv
```

8. create python virtual environment
```
python3 -m -venv env
```

9. activate python virtual environment
```
source env/bin/activate
```

10. cd back until you reach ~$
```
cd ..
```

11. install nginx
```
sudo apt-get install -y nginx
```

12. install gunicorn
```
pip install gunicorn
```

13. check packages installed in your virtual environment
```
pip list
```

14. check your public ip address in a browser
```
00.000.000.000
```

15. install supervisor
```
sudo apt-get install supervisor
```

16. create configuration file for supervisor
```
cd /etc/supervisor/conf.d/
```
17. create gunicorn conf
```
sudo touch gunicorn.conf
sudo nano gunicorn.conf
```
```
[program:gunicorn]
directory=/home/ubuntu/customUserBlogProdInvApi01/core
command=/home/ubuntu/customUserBlogProdInvApi01/env/bin/gunicorn --workers 3 --bind unix:/home/ubuntu/customUserBlogProdInvApi01/core/app.sock core.wsgi:application  
autostart=true
autorestart=true
stderr_logfile=/var/log/gunicorn/gunicorn.err.log
stdout_logfile=/var/log/gunicorn/gunicorn.out.log

[group:guni]
programs:gunicorn	
```    
save and exit gunicorn.conf
```
ctrl+o
enter
ctrl+x
```    
18. create log for errors
```
sudo mkdir /var/log/gunicorn
```
19. tell supervisor about our gunicorn file
```
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl status
```

20. go back directory untill you reach inside /etc$
```
cd ..
```

21. setup nginx. go to nginx
```
cd nginx
```
22. setup nginx configuration
```
sudo nano nginx.conf
```
23. change `www-data` into `root`. Save and exit
24. go to sites-available
```
cd sites-available
```
25. setup django.conf. Add your public address in server_name	
```
sudo touch django.conf
sudo nano django.conf
```
```
server{

    listen 80;
    server_name 00.000.000.000;

    
    location / {

        include proxy_params;
        proxy_pass http://unix:/home/ubuntu/customUserBlogProdInvApi01/core/app.sock;

    }

}	
```
26. test configuration to make sure that everything is working as it should
```
sudo nginx -t
```
27. enable our site to make it live
```
sudo ln django.conf /etc/nginx/sites-enabled
sudo service nginx restart
```

28. visit your site in the browser
00.000.000.000