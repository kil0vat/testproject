from django.db import models

# Create your models here.

class Person(models.Model):
	name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	date_of_birth = models.CharField(max_length=10)
	bio = models.TextField()
	email = models.EmailField(max_length=20)
	jabber = models.CharField(max_length=20)
	skype = models.CharField(max_length=20)
	other_contacts = models.TextField()
