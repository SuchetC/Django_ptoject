from django.shortcuts import render
from django.http import HttpResponse

from train_fair.forms import enter_fare

# Create your views here.

def fare(Request):
    form = enter_fare()
    if Request.method == 'POST':
        form = enter_fare(Request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse("<h1>Record Inserted Successfully</h1>")
        else:
             print("ERROR FORM INVALID")
    return render(Request, 'train_fair/fare.html',  context={'form':form})
