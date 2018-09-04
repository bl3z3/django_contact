from contact.forms import ContactForm
from django.template.loader import get_template
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template import Context
from django.shortcuts import render,redirect

# Create your views here.
def contact(request):
	form_class  = ContactForm

	if request.method == 'POST':
		form = form_class(data=request.POST)

		if form.is_valid():
			contact_name = form.cleaned_data['contact_name']
			contact_email = form.cleaned_data['contact_email']
			form_content = form.cleaned_data['content']

			# email profile with content
			template = get_template('contact_template.txt')

			context = {
				'contact_name': contact_name,
				'contact_email': contact_email,
				'form_content': form_content,
			}
			content = template.render(context)
			email = EmailMessage(
				'New contact form submission',
				content,
				'Your website <hi@weddinglovely.com>',
				['patrickblaze2@gmail.com'],
				headers = {'Reply-To': contact_email }
			)
			email.send()
			messages.add_message(request, messages.SUCCESS, 'E-mail sent')
			return redirect('contact')

	return render(request, 'contact.html', {
		'form': form_class,
	})