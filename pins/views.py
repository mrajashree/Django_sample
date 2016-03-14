from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from pins.models import Pins, Category
from django.template import RequestContext, loader

# Create your views here.

def PinsDisplay(request):
	pins_list = Pins.objects.all().order_by('name')
	#output = ', '.join([x.name for x in pins_list])	#w/o template
	template = loader.get_template('pins/PinsDisplay.html')
	context = {
		'pins_list': pins_list,
	}
	return HttpResponse(template.render(context,request))

def PinDescription(request,id):
	pin = Pins.objects.filter(id=id)#.values('description')
	#pin = pin[0]['description']
	description = pin.values('description')[0]['description']
	category = pin.values('category')[0]['category']
	pin_id = pin.values('id')[0]['id']
	category = Category.objects.filter(id=category).values('name')[0]['name']
	template = loader.get_template('pins/PinDescription.html')
	context = {
		'description': description,
		'category': category,
		'pin_id': pin_id,
	}
	return HttpResponse(template.render(context,request))
