from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Review(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=450)
    rating = models.IntegerField(
        validators=[
            MinValueValidator(0, "Rating cannot be less than 0."),
            MaxValueValidator(5, "Rating cannot be greater than 5.")
        ]
    )

    def __str__(self):
        return self.content


class News(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=1000)
    img_path = models.CharField(max_length=200)

