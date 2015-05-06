from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=30)
    icon  = models.ImageField()

    def __unicode__(self):
        return self.title

class Event(models.Model):
    category    = models.ForeignKey(Category, default=0)
    title       = models.CharField(max_length=30)
    logo        = models.ImageField()
    background  = models.ImageField()
    brand       = models.BooleanField()
    description = models.TextField()
    video       = models.TextField()
    begin       = models.DateField()
    end         = models.DateField()


    def __unicode__(self):
        return self.title
