from django.forms import ModelForm
from fuzail_app.models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["first_name","last_name","subject","email","message"]