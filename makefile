install:
	pip install -r requirements.txt

migrations:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

createapp:
	python manage.py startapp

superuser:
	python manage.py createsuperuser

shell: 
	python manage.py shell

serve:
	python manage.py runserver

collectstatic:
	python manage.py collectstatic

test: 
	python manage.py test