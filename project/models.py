from django.db import models

# Create your models here.
class Clothing(models.Model):
    text = models.TextField(blank=True)
    image_url = models.URLField(blank=True)

    def __repre__(self):
        return self.text