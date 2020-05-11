# Generated by Django 3.0.5 on 2020-04-22 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('category', models.CharField(choices=[('phy_health', 'PHYSICAL HEALTH'), ('ment_health', 'MENTAL HEALTH'), ('muscle_development', 'MUSCLE DEVELOPMENT')], max_length=20)),
                ('title', models.CharField(blank=True, max_length=50)),
                ('blog_image', models.ImageField(upload_to='images/blogs', verbose_name='Image')),
                ('content', models.TextField(max_length=1000)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
            },
        ),
    ]
