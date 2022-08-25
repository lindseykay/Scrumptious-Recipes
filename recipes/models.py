from django.db import models


# Create your models here.
# if you have nothing in your class/model,
# Django automatically gives the instance an ID integer


# when you update models:
# 1. update the model/ create the model
# 2. make migrations


class Recipe(models.Model):
    name = models.CharField(max_length=125)
    author = models.CharField(max_length=100)
    description = models.TextField()
    image = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + " by " + self.author


class Measure(models.Model):
    name = models.CharField(max_length=30, unique=True)
    abbreviation = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.abbreviation


class FoodItem(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    amount = models.FloatField()
    recipe = models.ForeignKey(
        "Recipe", related_name="ingredients", on_delete=models.CASCADE
    )
    measure = models.ForeignKey("Measure", on_delete=models.PROTECT)
    food = models.ForeignKey("FoodItem", on_delete=models.PROTECT)

    def __str__(self):
        amount_str = str(self.amount)
        return f"{amount_str} {self.measure.abbreviation} {self.food.name}"


class Step(models.Model):
    recipe = models.ForeignKey(
        "Recipe", related_name="steps", on_delete=models.CASCADE
    )
    order = models.PositiveSmallIntegerField()
    directions = models.CharField(max_length=300)

    def __str__(self):
        str_order = str(self.order)
        return "step " + str_order
