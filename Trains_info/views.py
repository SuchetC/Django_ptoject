from django.shortcuts import render
from django.http import HttpResponse
from Trains_info.models import train_details
from Trains_info import  forms
# Create your views here.e

def home(Request):
    return  render(Request, "Trains_info\home.html")

def collect_train_info(Request):
    form = forms.train_form()
    if Request.method == 'POST':
        form = forms.train_form(Request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse("<h2>Record Updated to Train_details Table </h2>")
        else:
            return  HttpResponse("Error ")

    return render(Request, "Trains_info\info.html" , context=dict({'form_d' : form}))

def report(Request):
    train_mdl_details = train_details.objects.order_by('train_num')
    train_details_dict = {'insert_train_details':train_mdl_details}

    return render(Request , r"Tra   ins_info\repots.html" , context=train_details_dict)

