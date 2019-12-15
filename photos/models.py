from django.db import models

# Create your models here.
class Image(models.Model):

    img = models.ImageField(upload_to = 'images/', default='path/to/my/default/image.jpg')
    img name = models.CharField(max_length =30)
    img description = models.TextField()
    location = models.ForeignKey('Location',on_delete=models.CASCADE)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)

    def __str__(self):
        return self.img
