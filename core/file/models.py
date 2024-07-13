from django.db import models

# Create your models here.
class File(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to="files/")

    def delete(self):
        self.image.delete()
        super().delete()