from django.db import models

# Create your models here.
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

    @classmethod
    def search_by_category(cls,search_term):
        photos = cls.objects.filter(category__name__icontains=search_term)
        return photos
    @classmethod
    def filter_by_location(cls,location_term):
        location=cls.objects.filter(location__location_name__icontains=location_term)
        return location

    @classmethod
    def get_image_by_id(cls,id):
        try:
            image = cls.objects.get(id=id)
            print("Object Found")
            return image
        except DoesNotExist:
            print("Object Not Found")

    
