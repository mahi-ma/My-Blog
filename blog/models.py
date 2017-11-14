from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

