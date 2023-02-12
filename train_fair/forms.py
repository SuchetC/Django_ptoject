from django import forms
from train_fair.models  import fare

class enter_fare(forms.ModelForm):
    class Meta:
        model  = fare
        fields = '__all__'