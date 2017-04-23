export LC_CTYPE="en_US.UTF-8"

run:
	python ./manage.py runserver

migrate:
	python manage.py migrate