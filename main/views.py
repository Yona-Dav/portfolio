from django.shortcuts import render
from .models import Contact
from .forms import ContactForm
from django.views.generic import CreateView
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

# Create your views here.

def contact_thanks(request):
    return render(request, 'contact_received.html')


class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'homepage.html'

    def form_valid(self, form):
        self.object = form.save()
        name = self.object.name

        mail_subject = 'Contact Message'
        message = render_to_string('contact_email.html', {
            'user': self.object,
        })
        from_email = form.cleaned_data.get('email')
        email = EmailMessage(
            mail_subject, message, from_email=from_email, to=['yonabohbot@gmail.com']
        )
        email.send()

        return render(self.request, 'contact_received.html', {'name':name})
