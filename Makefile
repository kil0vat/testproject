MANAGE=django-admin.py

test:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=ticket1.settings $(MANAGE) test contact_info
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=ticket1.settings $(MANAGE) collectstatic --noinput
run:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=ticket1.settings $(MANAGE) runserver

syncdb:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=ticket1.settings $(MANAGE) syncdb --noinput
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=ticket1.settings $(MANAGE) migrate
