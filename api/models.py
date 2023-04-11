from django.db import models

size_choice = (
    ("Tiny", "Tiny"),
    ("Small", "Small"),
    ("Medium", "Medium"),
    ("Large", "Large"),
)

friendliness_choice = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)

trainability_choice = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)
sheddingamount_choice = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)

exerciseneeds_choice = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)

class Breed(models.Model):
    name = models.CharField(max_length=25, primary_key=True)
    size = models.CharField(max_length=10,choices=size_choice)
    friendliness = models.IntegerField(choices=friendliness_choice)
    trainability = models.IntegerField(choices=trainability_choice)
    sheddingamount = models.IntegerField(choices=sheddingamount_choice)
    exerciseneeds = models.IntegerField(choices=exerciseneeds_choice)

    def __str__(self):
        return self.name

gender_choices = (
    ("male", "male"),
    ("female", "female"),
    ("none", "None"),
)

class Dog(models.Model):
    name = models.CharField(max_length=25)
    age = models.IntegerField()
    breed = models.ForeignKey(Breed,on_delete=models.CASCADE)
    gender = models.CharField(max_length=7,choices=gender_choices)
    color = models.CharField(max_length=10)
    favoritefood = models.CharField(max_length=10)
    favoritetoy = models.CharField(max_length=10)

    def __str__(self):
        return self.name