from django.db import models
# from tinymce.models import HTMLField

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField(blank = True)
    image = models.ImageField(upload_to = "photos/%Y/%m/%d/")
    # content = HTMLField()

    def __str__(self):
        return self.title