from django.db import models
from taggit.managers import TaggableManager
from django.utils.datetime_safe import datetime
from django.dispatch import receiver
from django.db.models.signals import post_save
import numpy as np
from django.contrib.auth.models import User


# Create your models here. 
#////////////////////-------User and profile////////////////////////////////////


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()






#////////////////////----Product-Model -----////////////////////////////////////////////////////////////////////////////////
class Products(models.Model):


  #  effect choices
    UPLIFTED = 'UP'
    HAPPY = 'HA'
    RELAXED ='RE'
    ENERGETIC='EN'
    CREATIVE ='CE'
    FOCUSED ='FO'  
    TALKATIVE ='TA'
    EUPHORIC='EU'
    GIGGLY ='GI'
    HUNGRY ='HU'
    AROUSED ='AR'
    TINGLY= 'TI'  
    SLEEPY= 'SL'

    Effects_Choices = [
        (UPLIFTED, 'Uplifted'),
        (HAPPY, 'Happy'),
        (RELAXED, 'Relaxed'),
        (ENERGETIC, 'Energetic'),
        (CREATIVE,'Creative' ),
        (FOCUSED,'Focused'),
        (TALKATIVE,'Talkative'),
        (EUPHORIC, 'Euphoric'),
        (GIGGLY, 'Giggly'),
        (HUNGRY, 'Hungry'),
        (AROUSED, 'Aroused'),
        (TINGLY, 'Tingy'),
        (SLEEPY, 'Sleepy')]

    #catagories choices ///////////////////////////////////////////////////////////////////////////////
    POLLEN ='PL'
    FEM_POLLEN ='FP'
    SEEDS = 'SD'
    FEM_SEEDS ='FS'
    AUTO_SEEDS ='AS'
    FLOWER ='FL'
    CONCENTRATES ='CS'
    EDIBLES ='ES'

    Catagories_Choices =[
        (POLLEN,'Pollen'),
        (FEM_POLLEN, 'Feminized Pollen'),
        (SEEDS, 'Seeds'),
        (FEM_SEEDS,'Feminized Seeds'),
        (AUTO_SEEDS, 'Auto Flowering Seeds'),
        (FLOWER, 'Flower'),
        (CONCENTRATES,'Concentrates'),
        (EDIBLES, 'Edibles')]



    #variety
    SATIVA ='SA'
    INDICA ='IN'
    HYBRID ='HY'
    
    Variety_choices =[
        (SATIVA, 'Sativa'),
        (INDICA, 'Indica'),
        (HYBRID, 'Hybrid')]


    name        = models.CharField(max_length = 30)
    catagory    = models.CharField(max_length = 30, choices=Catagories_Choices)
    variety     = models.CharField(max_length= 2, choices=Variety_choices)
    price 		= models.DecimalField(decimal_places=2, max_digits=20, default=0.00)
    quantity 	= models.IntegerField()
    Image 		= models.ImageField(default="Null")
    description = models.CharField(max_length= 256, blank=True, null=True)
    effects     = models.CharField(max_length= 2 ,choices=Effects_Choices)

    objects =models.Manager()

    Review = models.ForeignKey('Review', on_delete=models.CASCADE,blank=True ,null=True)
    tags = TaggableManager()

    

    def average_rating(self):
        all_ratings = map(lambda x: x.rating, self.review_set.all())
        return np.mean(all_ratings)
        

    def __str__(self):
        return self.name,self.price
    class Meta:
        indexes =[
            models.Index(fields=['name'])
        ]
#///////////////////////----Review-Model---/////////////////////////////////////


class Review(models.Model):
    rating_choices = zip(range(6), range(6))
    item         = models.ForeignKey(Products, on_delete=models.CASCADE)
    pub_date     = models.DateTimeField('date published')
    user         = models.CharField(max_length=100)
    comment      = models.CharField(max_length=200)
    rating       = models.IntegerField(choices=rating_choices)

    def __str__(self):
        return ( )




 

#////////////////////////////-----Cart--------///////////////////////////////////////////////////////////////////
class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)
    total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    updated = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "User: {} has {} items in their cart. Their total is ${}".format(self.user , self.count, self.total)

#/////////////////////----------Entry-------------------///////////////////////////////////////
class Entry(models.Model):
    product = models.ForeignKey(Products, null=True, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, null=True, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return"This entry contains {} {}(s).".format(self.quantity, self.product.name)


@receiver(post_save, sender=Entry)
def update_cart(sender, instance, **kwargs):
    line_cost = instance.quantity * instance.product.line.cost
    instance.cart.total += line_cost
    instance.cart.count += instance.quantity
    instance.cart.updated = datetime.now()
#//////////////////////////////////////////////////////////////////////////////////////////////