# phishing-detection
Phishing detection chrome extension

# Django key exposed
`pip3 install python-dotenv`

create .env file in root backend rootfolder

add the line `SECRET_KEY = '7o&q@=gx652hinx%tm5^a)hi%ufw=n^9(cm00=7@-ej@(ymey%'`

in setting.py

`import os`

`from dotenv import load_dotenv`

`load_dotenv()`

`SECRET_KEY = str(os.getenv('SECRET_KEY'))`

# install whois
`pip install python-whois` 
