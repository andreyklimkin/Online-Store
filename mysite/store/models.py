# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
    def __str__(self):
        return self.question_text

class Watches_Main(models.Model):
    image=models.ImageField(upload_to='images', null=True)
    model=models.CharField(max_length=200)
    #order=models.IntegerField(default=0)
    def __str__(self):
        return self.model

class Watches_Men(models.Model):
    image=models.ImageField(upload_to='images', null=True)
    model=models.CharField(max_length=200)
    firm=models.CharField(max_length=200)
    #order=models.IntegerField(default=0)
    def __str__(self):
        return self.model

class Watches_Women(models.Model):
    image=models.ImageField(upload_to='images', null=True)
    model=models.CharField(max_length=200)
    firm=models.CharField(max_length=200)
    #order=models.IntegerField(default=0)
    def __str__(self):
        return self.model

class Collection_Model(models.Model):
    image=models.ImageField(upload_to='images', null=True)
    model=models.CharField(max_length=200)
    firm=models.CharField(max_length=200)
    #order=models.IntegerField(default=0)
    def __str__(self):
        return self.model