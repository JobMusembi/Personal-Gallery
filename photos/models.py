from django.db import models

# Create your models here.
class Image(models.Model):

    img = models.ImageField(upload_to = 'images/', default='path/to/my/default/image.jpg')
    img_name = models.CharField(max_length =30)
    img_description = models.TextField()
    location = models.ForeignKey('Location',on_delete=models.CASCADE)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)

    def __str__(self):
        return str(self.img)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        self.update()

    @classmethod
    def photos_display(cls):
        photos = cls.objects.filter()
        return photos

class category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

class location(models.Model):
    location_name = models.CharField(max_length =30)

    def __str__(self):
        return self.location_name

    def save_location(self):
        self.save()
