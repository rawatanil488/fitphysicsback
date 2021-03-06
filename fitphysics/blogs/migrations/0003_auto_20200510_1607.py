# Generated by Django 3.0.5 on 2020-05-10 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20200510_1607'),
        ('blogs', '0002_blog_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='profiles.UserProfile'),
        ),
    ]
