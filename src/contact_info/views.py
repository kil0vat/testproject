from src.contact_info.models import Person
from django.shortcuts import render
from django.template import loader, RequestContext
from django.http import HttpResponse
# Create your views here.

def base(request):
	person_list = Person.objects.all()
	template = loader.get_template('contact_info/base.html')
	context = RequestContext(request, {
		'person_list': person_list,
	})
	return HttpResponse(template.render(context))
