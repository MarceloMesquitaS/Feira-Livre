Para windows: 
Instale módulos viaVENV

$ python -m venv venv   
$ .\venv\Scripts\activate 
$ pip install -r requirements.txt

Configurar banco de dados

$ python manage.py makemigrations
$ python manage.py migrate

Iniciar o aplicativo

$ python manage.py runserver
