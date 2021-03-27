python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install django split-settings django-allauth
pip freeze > requirements.txt
django-admin startproject project --verbosity 2 --template ./conf/project_template
cd project/apps
django-admin startapp core --verbosity 2 --template ../../conf/app_template
django-admin startapp accounts --verbosity 2 --template ../../conf/account_template
cd ..
python3 manage.py makemigrations
python3 manage.py migrate 
python3 manage.py collectstatic
python3 manage.py makemessages --ignore venv --all
python3 manage.py compilemessages
python3 manage.py collectstatic
python3 manage.py runserver