# django-drf-todo
TODO app backend using django and django rest framework

### This backend is hosted on Heruko:
https://django-drf-todo.herokuapp.com/docs/
### To run the project locally
```
mkdir todo
cd todo
python3 -m venv venv
source venv/scripts/activate
git clone https://github.com/AkramYamin/django-drf-todo.git
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```