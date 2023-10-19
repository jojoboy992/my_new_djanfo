from django.db import models

YEAR_IN_SCHOOL =[
        ("FR","French man"),
        ("JR", "Junior"),
        ("SR","Senior")
    ]


class Musician(models.Model):
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    instrument = models.CharField(max_length=20)
    artist_name = models.CharField(max_length=20)
    level = models.CharField(max_length=20, choices=YEAR_IN_SCHOOL)
   
    def __str__(self) -> str:
        return self.artist_name


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    release_dtae = models.DateField()
    num_stars = models.IntegerField()

    def __str__(self) -> str:
        return self.name


# Create your models here.
