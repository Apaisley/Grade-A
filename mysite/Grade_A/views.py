from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Products
from .models import Review
import datetime

def index(request):
    products = Products.objects.all()
    product_names = list()
    
    for product in products:
        product_names.append(product.name)
    response_html ='<br>'.join(product_names)
    return HttpResponse(" Welcome to the Grade A website"+response_html)



def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
    user.save()