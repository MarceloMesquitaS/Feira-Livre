<br />

Configurar para Windows
Install modules via VENV

$ python -m venv venv   
$ .\venv\Scripts\activate 
$ pip install -r requirements.txt


<br />

Configurar banco de dados

$ python manage.py makemigrations
$ python manage.py migrate


<br />

Inicie o aplicativo

$ python manage.py runserver


Neste ponto, o aplicativo é executado em http://127.0.0.1:8000/. 


<br />
