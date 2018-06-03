from django.db import models
from datetime import date
from django.urls import reverse

# Create your models here.
class Scores(models.Model):
    Game_No = models.AutoField(primary_key=True)
    Date = models.DateField(default=date.today)
    Abhinav = models.IntegerField()
    Harshith = models.IntegerField()
    Rajath = models.IntegerField()
    Winner = models.CharField(max_length=50)
    deal = models.CharField(default='N', max_length=1)

    def __str__(self):
        return "Game :" + str(self.Game_No) + " Abinav-" + str(self.Abhinav) + " Harshith-" + str(self.Harshith) + " Rajath-" + str(self.Rajath) + " Winner-" + self.Winner

    def get_absolute_url(self):
        return reverse('score:index')

    class Meta:
        verbose_name_plural = "Scores"