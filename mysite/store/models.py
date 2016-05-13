# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Brands(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Collections(models.Model):
    name=models.CharField(max_length=200)
    brand=models.ForeignKey(Brands, null=True)
    def __str__(self):
        return self.name


class Watches(models.Model):
    model=models.CharField(max_length=200)
    brand=models.ForeignKey(Brands, null=True)
    collection=models.ForeignKey(Collections, null=True)
    GENDER_CHOICES = (
        (u'M', u'Male'),
        (u'F', u'Female'),
    )
    rating=models.IntegerField(default=0)
    prize=models.IntegerField(default=0)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    image=models.ImageField(upload_to='images', null=True)
    def __str__(self):
        return self.model


class Collection_Model(models.Model):
    image=models.ImageField(upload_to='images', null=True)
    model=models.CharField(max_length=200)
    firm=models.CharField(max_length=200)
    #order=models.IntegerField(default=0)
    def __str__(self):
        return self.model

class Carts(models.Model):
    user_name=models.ForeignKey(User, null=True)
#   model=models.CharField(max_length=200)
#   firm=models.CharField(max_length=200)
#   #order=models.IntegerField(default=0)
#   def __str__(self):
#        return self.model
    def __str__(self):
        return self.user_name.username

class Cart_Items(models.Model):
    cart=models.ForeignKey(Carts, null=True)
    item=models.ForeignKey(Watches, null=True)