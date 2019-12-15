from django.test import TestCase
from .models import Image,category,location
# Create your tests here.

class categoryTestClass(TestCase):

    def setUp(self):
        self.outdoor = category(name = 'outdoor')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.outdoor,category))

    # Testing Save Method
    def test_save_method(self):
        self.outdoor.save_category()
        categories = category.objects.all()
        self.assertTrue(len(categories) > 0)

class locationTestClass(TestCase):

    def setUp(self):
        self.nairobi = location(location_name = 'Nairobi')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi,location))

    # Testing Save Method
    def test_save_method(self):
        self.nairobi.save_location()
        locations = location.objects.all()
        self.assertTrue(len(locations) > 0)


class ImageTestClass(TestCase):

    def setUp(self):

        #creating a new category and saving it
        self.outdoor = category(name = 'outdoor')
        self.new_category.save_category()

        #creating a new location and saving it
        self.nairobi = location(location_name = 'Nairobi')
        self.new_location.save_location()

        #creating a new image post and saving it
        self.new_image = Image(img = 'img.jpg', img_name = 'Test Name', img_description = 'Test Description', location = self.nairobi, category = self.outdoor)

    def tearDown(self):
        Image.objects.all().delete()
        category.objects.all().delete()
        location.objects.all().delete()
