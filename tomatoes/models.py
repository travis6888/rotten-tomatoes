from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100, null=True)
    release_year = models.PositiveSmallIntegerField(null=True)
    critic_rating = models.IntegerField(null=True)
    poster = models.URLField(null=True)
    mpaa_rating = models.CharField(max_length=40, null=True)
    runtime = models.PositiveSmallIntegerField(null=True)
    audience_score = models.IntegerField(null=True)

    def __unicode__(self):
        return self.title