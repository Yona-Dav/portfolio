from .models import Contact
from django import forms
from django import forms
from captcha.fields import ReCaptchaField



class ContactForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Contact
        fields = '__all__'