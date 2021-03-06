from __future__ import unicode_literals

from django.db import models
import datetime

from MediaServer.upload import rand_key
from Shop.models import Order,Contact

# Create your models here.


YEAR_CHOICES = [(r,r) for r in range(datetime.datetime.now().year, datetime.datetime.now().year+11)]
MONTH_CHOICES = [(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10),(11,11),(12,12)]

# Details for logging in to the api
class PaymentProvider(models.Model):
    api = models.CharField(max_length=100)
    user_name = models.CharField(max_length=40)
    secret = models.CharField(max_length=50)

# method like paypal and sofort
class PaymentMethod(models.Model):
    name = models.CharField(max_length=30)
    details = models.CharField(max_length=500,default='')
    provider = models.ForeignKey(PaymentProvider,blank=True,null=True)

class CardType(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class PaymentDetails(models.Model):
    order = models.ForeignKey(Order)
    method = models.ForeignKey(PaymentMethod)
    user = models.ForeignKey(Contact,blank=True)

#TODO: a credit card should belong to an user or company
class CreditCard(PaymentDetails):
    card_type = models.ForeignKey(CardType)
    name = models.CharField(max_length=70)
    card_number = models.CharField(max_length=20)
    expiry_year = models.IntegerField(  choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    expiry_month = models.IntegerField(  choices=MONTH_CHOICES, default=datetime.datetime.now().month)
    cvv = models.IntegerField(max_length=3)

class Bill(PaymentDetails):
    pass



# The object for orders to determine wether order has been paid or not and stuff
class Payment(models.Model):
    is_paid = models.BooleanField()
    token = models.CharField(max_length=30)
    details =models.ForeignKey(PaymentDetails)
