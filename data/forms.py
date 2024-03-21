from django import  forms
from data.models import Details

class Forms(forms.Form):
    f_name = forms.CharField()
    l_name = forms.CharField()
    email= forms.EmailField()
    city = forms.CharField()
    state  = forms.ChoiceField(choices=[('Ap' , 'Andhra Pradesh'), ('Ts', 'Telangana')])
    zip_code = forms.IntegerField()
    agree = forms.BooleanField()

class MyForm(forms.ModelForm):
    class Meta:
        model = Details
        fields = ['firstname', 'lastname', 'username', 'city', 'state', 'zipcode']
