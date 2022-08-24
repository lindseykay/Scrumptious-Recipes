from django.contrib import admin


# Register your models here.
from recipes.models import Recipe
from recipes.models import Measure
from recipes.models import FoodItem

admin.site.register(Recipe)
admin.site.register(Measure)
admin.site.register(FoodItem)
