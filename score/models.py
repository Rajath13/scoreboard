"""Models module and date from datetime module to add default date in model"""
from datetime import date
from django.db import models
from django.urls import reverse

# Create your models here.
class Scores(models.Model):
    """Model for the scoreboard"""
    Game_No = models.AutoField(primary_key=True)
    Date = models.DateField(default=date.today)
    Session = models.IntegerField(default=0)
    Abhinav = models.IntegerField()
    Harshith = models.IntegerField()
    Rajath = models.IntegerField()
    Winner = models.CharField(max_length=50)
    deal = models.CharField(default='N', max_length=1)

    def __str__(self):
        return "Game :" + str(self.Game_No) + " Winner-" + self.Winner

    def get_absolute_url(self):
        """Redirect to index view after form submit"""
        return reverse('score:index')

    class Meta:
        verbose_name_plural = "Scores"
