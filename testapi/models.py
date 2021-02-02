from django.db import models


# Create your models here.

class Animal(models.Model):
    name = models.CharField(max_length=50)
    sound = models.CharField(max_length=50)

    class Meta:
        db_table = 'animal'

    def speak(self):
        return f'The {self.name} says "{self.sound}"'

    @staticmethod
    def square(number):
        return number ** 2
