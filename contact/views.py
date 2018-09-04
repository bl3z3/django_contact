from contact.forms import ContactForm
from django.shortcuts import render

# Create your views here.
def contact(request):
	form_class  = ContactForm

	return render(request, 'contact.html', {
		'form': form_class,
	})