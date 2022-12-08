from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        # if img.height > 600 or img.width > 600:
        #     # if min(img.height, img.width) < 800:
        #     #     new_img = (min(img.height, img.width), min(img.height, img.width))
        #     # else:
        new_img = (800, 800)
        img = img.resize((new_img))
        img.thumbnail(new_img)
        img.save(self.avatar.path)
