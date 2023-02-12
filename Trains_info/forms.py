from django import forms
from Trains_info.models import train_details
class train_form(forms.ModelForm):
    # train_num = forms.IntegerField()
    # train_name = forms.CharField()
    # origin_city = forms.CharField()
    # destination_city = forms.CharField()
    # departure_time = forms.TimeField()
    # arival_time = forms.TimeField()
    class Meta:
        model = train_details
        fields = '__all__'



