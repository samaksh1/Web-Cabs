from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
HOSTELS=[
        ('Brahmaputra', 'Brahmaputra'),
        ('Dihing', 'Dihing'),
        ('Manas', 'Manas'),
        ('Lohit', 'Lohit'),
        ('Dhansiri', 'Dhansiri'),
        ('Kapili', 'Kapili'),
        ('Siang', 'Siang'),
        ('Kameng', 'Kameng'),
        ('Umiam', 'Umiam'),
        ('Barak', 'Barak'),
        ('Subhansiri', 'Subhansiri'),
        ('Disang/Dibang', 'Disang/Dibang'),
]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hostel = models.CharField(blank=False, max_length=50 ,choices=HOSTELS)
    profile_pic = models.ImageField(blank=True, default='default.jpg', upload_to='profile_pics')
    # add any gender-neutral photo in default

    def __str__(self):
        return self.user.username

    # def get_absolute_url(self):
    #     return reverse('accounts:user_detail' , kwargs={'pk':self.pk})
