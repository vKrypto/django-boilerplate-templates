python3.9 -m venv venv
source venv/bin/activate
pip install django split-settings
pip freeze > requirements.txt
django-admin startproject project --verbosity 2 --template ./conf/project_template
cd project
django-admin startapp core --verbosity 2 --template ../conf/app_template
django-admin startapp account --verbosity 2 --template ../conf/app_template
python3 manage.py makemigrations
python3 manage.py migrate 
python3 manage.py collectstatic
python3 manage.py makemessages --ignore venv
python3 manage.py compilemessages
python3 manage.py runserver

