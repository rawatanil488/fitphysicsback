import uuid
from django.db import models
from django.utils import timezone
from ..profiles.models import UserProfile

class Blog(models.Model):
    category_choices = (
        ('phy_health', 'PHYSICAL HEALTH'),
        ('ment_health', 'MENTAL HEALTH'),
        ('muscle_development', 'MUSCLE DEVELOPMENT'),
    )
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    author = models.ForeignKey(UserProfile, on_delete=models.PROTECT)
    created_on = models.DateTimeField(default = timezone.now)
    category = models.CharField(max_length=20, choices=category_choices)
    title = models.CharField(max_length=50, blank=True)
    blog_image = models.ImageField('Image', upload_to='images/blogs', blank=False)
    content = models.TextField(max_length=1000, blank=False)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
