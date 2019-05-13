virtualenv --python=/usr/bin/python3.7 venv
source venv/bin/activate

pip install django
pip install graphene_django
pip install django_graphiql

./manage.py makemigrations
./manage.py migrate
./manage.py runserver