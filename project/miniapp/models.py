from django.db import models

class datainsert(models.Model):
    name = models.CharField(max_length=200, default="x")
    title = models.CharField(max_length=200, default="x")
    play = models.CharField(max_length=200, default="x")

class post(models.Model):
    author = models.CharField(max_length=200, default="x")
    title = models.CharField(max_length=200, default="x")
    Mood = models.CharField(max_length=200, default="x")


class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2, default="")
