import uuid
from django.db import models
from ..users.models import User


class UserProfile(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    age = models.CharField(max_length=30, blank=True)
    telephone_number = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    image = models.ImageField('Image', upload_to='images/profile/', blank=True)

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfiles'
