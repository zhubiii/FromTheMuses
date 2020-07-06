from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    bio = models.TextField(blank=True, max_length=500)
    field_of_interest = models.CharField(blank=True, max_length=50)

    def __str__(self):
        return f'{self.user.username} Profile'

    def get_absolute_url(self):
        return reverse("profiles:User-Profile", kwargs={'username': self.user.username})

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)
        if img.height >200 or img.width > 200:
            output_size = (200,200)
            img.thumbnail(output_size)
            img.save(self.image.path)