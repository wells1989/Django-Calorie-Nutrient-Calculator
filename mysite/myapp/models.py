from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=250)
    carbs = models.FloatField()
    protein = models.FloatField()
    fats = models.FloatField()
    calories = models.IntegerField()

    def __str__(self):
        return self.name
    

class Consume(models.Model):
    user = models.ForeignKey(User, on_delete =models.CASCADE) # User = built in model in django (e.g. superuser via create-admin)
    food_consumed = models.ForeignKey(Food, on_delete=models.CASCADE) # foreign key, primary key of the Food item, on_delete ensures if the food primary key is deleted the foreign key is also deleted
    # note: if wanting to save a list of Food objects to one food_consumed, food_consumed = models.ManyToManyField(Food)  

    