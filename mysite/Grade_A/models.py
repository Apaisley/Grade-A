from django.db import models
from django.forms import ModelForm
from PIL import Image
import datetime
import numpy as np
from polymorphic.models import polymorphicModel
# Create your models here.

class Product_inventory(polymorphicModel):
    name = models.CharField(models=30)
    catagory    =
    Price 		= models.DecimalField(decimal_places=2, max_digits=20, default=0.00)
    Quantity 	= models.IntegerField()
	Type 		= models.CharField(max_length=10)
	Image 		= models.ImageField(default="Null")


    def average_rating(self):
        all_ratings = map(lambda x: x.rating, self.review_set.all())
        return np.mean(all_ratings)
        
    def __unicode__(self):
        return self.name


class Strain(Product_inventory):
    effects
    flavors
    types
   
    



class Breeder()


class Grower()

    









class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    product      = models.ForeignKey(Product)
    pub_date     = models.DateTimeField('date published')
    user_name    = models.CharField(max_length=100)
    comment      = models.CharField(max_length=200)
    rating       = models.IntegerField(choices=RATING_CHOICES)




 

#///////////////////////////////////////////////////////////////////////////////////////////////






#//////////////////////////////////////////////////////////////////////////////////////////////


