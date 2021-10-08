# phishing-detection
Phishing detection chrome extension

# install Django
`python -m pip install Django`

# Django run server

cd to backend/mysite

`python manage.py runserver`

# install django-cors-headers
`pip install django-cors-headers`

# Django key exposed
`pip3 install python-dotenv`

create .env file in root backend rootfolder

generate a Django Secret Key

add the line `SECRET_KEY = YOUR_KEY`

in setting.py

`import os`

`from dotenv import load_dotenv`

`load_dotenv()`

`SECRET_KEY = str(os.getenv('SECRET_KEY'))`

# install whois
`pip install python-whois` 

# install PyFunceble
`pip install --upgrade --pre pyfunceble-dev`

# install lxml
`pip install lxml`

# install selenium
`pip install selenium`
