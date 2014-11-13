MANAGE=django-admin.py

test:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=ticket1.settings $(MANAGE) test contact_info

run:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=ticket1.settings $(MANAGE) runserver

syncdb:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=ticket1.settings $(MANAGE) syncdb --noinput
