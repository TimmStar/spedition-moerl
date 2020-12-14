from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def index(request):
    return render(request, "app1/base.html", {})



def bestellung(request):
    if request.method =="GET":
        template = 'app1/bestellung.html'
        kundends = Kunde.objects.all()
        return render(request,template,{'kunden':kundends})
    else:
        button = request.POST['button']
        if button == "cancel":
            return redirect("/")
        elif button == "new":
            template = 'app1/bestellung.html'
            kundends = Kunde.objects.all()
            return render(request,template,{'kunden':kundends})           
        else:
            bestellungen = request.POST['bestellung'] 
            kunde = Kunde.objects.get(id=(request.POST['kunde']))
            ds = Bestellung(bestellung=bestellungen,kunde=kunde)
            ds.save()
            template = 'app1/erfolgreich.html'
            return render(request,template,{})