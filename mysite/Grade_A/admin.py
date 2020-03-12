from django.contrib import admin

# Register your models here.
from .models import Products
from .models import Review
from .models import Cart

admin.site.register(Products)
admin.site.register(Review)
admin.site.register(Cart)