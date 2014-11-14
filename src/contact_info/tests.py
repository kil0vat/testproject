"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from ticket1.contact_info.models import Person

class HttpTest(TestCase):
	def test_base(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)
		
	def setUp(self):
		self.person_contact = []
		person = Person.objects.create(
			name = "Test_name",
			last_name = "Test_last_name",
			date_of_birth = "Test_date_of_birth",
			bio = "Test_bio",
			email = "Test_email",
			jabber = "Test_jabber",
			skype = "Test_skype",
			other_contacts = "Test_other_contacts",
		)
		self.person_contact.append(person)
	
	def test_person_out(self):
		response = self.client.get('/')
		self.assertIn(self.person_contact[0].name, response.content)
		self.assertIn(self.person_contact[0].last_name, response.content)
		self.assertIn(self.person_contact[0].date_of_birth, response.content)
		self.assertIn(self.person_contact[0].bio, response.content)
		self.assertIn(self.person_contact[0].email, response.content)
		self.assertIn(self.person_contact[0].jabber, response.content)
		self.assertIn(self.person_contact[0].skype, response.content)
		self.assertIn(self.person_contact[0].other_contacts, response.content)
