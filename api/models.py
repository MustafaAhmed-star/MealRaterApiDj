from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.

class Meal(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)

    def no_of_ratings(self):
        ratings = Rater.objects.filter(meal=self)
        return len(ratings)
    
    def avg_rating(self):
        # sum of ratings stars  / len of rating hopw many ratings 
        sum = 0
        ratings = Rater.objects.filter(meal=self) # no of ratings happened to the meal 

        for x in ratings:
            sum += x.stars

        if len(ratings) > 0:
            return sum / len(ratings)
        else:
            return 0
    def __str__(self):
        return self.title

class Rater(models.Model):
    meal  = models.ForeignKey(Meal , on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ##add comment on meal 
    review = models.TextField(blank=True,null=True,max_length=250)
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    def __str__(self):
        return f'{self.user} rate {self.meal}'    
    

    class Meta:
        unique_together=(('user','meal'))
        index_together=(('user','meal'))