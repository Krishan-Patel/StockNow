from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from stocks.models import Stock
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def Home(request, *args, **kwargs):
    data = Stock.objects.all()
    if not data:
        data = loadData()
        for stock in data:
            obj = Stock()
            obj.identifier = stock['symbol']
            obj.day_high = float(stock['dayHigh'])
            obj.day_low = float(stock['dayLow'])
            obj.current = float(stock['lastPrice'])
            obj.change = float(stock['change'])
            obj.pchange = float(stock['pChange'])
            obj.last_update = timezone.now()
            if stock['perChange365d'] == '-':
                obj.pchange365 = 0
            else :
                obj.pchange365 = float(stock['perChange365d'])
            obj.save()
            
    elif timezone.now() - data[0].last_update > timedelta(minutes=30):
        #print("update")
        stocks = Stock.objects.all()
        data = loadData()
        for i in range(len(stocks)):
            stocks[i].identifier = data[i]['symbol']
            stocks[i].day_high = data[i]['dayHigh']
            stocks[i].day_low = data[i]['dayLow']
            stocks[i].current = data[i]['lastPrice']
            stocks[i].change = data[i]['change']
            stocks[i].pchange = data[i]['pChange']
            stocks[i].last_update = timezone.now()
            stocks[i].save()
    else :
        #print('okay') 
        name = request.GET.get('search', False)
        if name:
            stock = Stock.objects.filter(identifier__iexact = name)
            if stock:
                return render(request, "index.html", context = {'stocks': stock})
            else: 
                return render(request, "index.html", context = {'error': "Invalid Stock Name"})
        
        if not request.user.is_anonymous:
            favourites = Stock.objects.filter(favourites=request.user)
            if favourites:
                return render(request, "index.html", context = {'saved': favourites})
            
        return render(request, "index.html", {})


import requests
def loadData():

    url = "https://latest-stock-price.p.rapidapi.com/price"

    querystring = {"Indices":"NIFTY 500"}
    headers = {
        'x-rapidapi-key': "a8e178be2bmsha9d8ae75567c9b5p1f8a0bjsn5002e7f662f5",
        'x-rapidapi-host': "latest-stock-price.p.rapidapi.com"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    response = response.json()
    return response

from django.views import generic
class StockListView(generic.ListView):
    model = Stock
    paginate_by = 25


@ login_required
def fav(request, id):
    obj = get_object_or_404(Stock, identifier=id)
    if obj.favourites.filter(id=request.user.id).exists():
        obj.favourites.remove(request.user)
    else: 
        obj.favourites.add(request.user)
    
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def register(request, *args, **kwargs):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=True)
        user.set_password(form.cleaned_data.get("password1"))
        # send a confirmation email to verify their account
        #login(request, user)
        return redirect("/")
    context = {
        "form": form,
        "btn_label": "Register",
        "title": "Register"
    }
    return render(request, "register.html", context)


    