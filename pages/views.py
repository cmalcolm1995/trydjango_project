from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
	my_home_context = {
		"home_desc": "Welcome to the home page, this is some context"
	}
	return render(request, 'home.html', my_home_context)


def contact_view(request, *args, **kwargs):
	my_context = {
		"my_text": "This is about contacts", 
		"my_number": 123,
		"my_list": [123,456,789, 65434, 765432112,45,754,222,567, "Extra"]
	}
	return render(request, 'contact.html', my_context)