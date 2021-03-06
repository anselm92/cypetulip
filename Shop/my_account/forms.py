from django.forms import ModelForm

from Shop.models import Contact, Company


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        exclude = ['company', 'user',]

class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        exclude = ['company_id', 'term_of_payment',]