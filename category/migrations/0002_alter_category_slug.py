# Generated by Django 4.2.7 on 2024-01-22 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=20, unique=True),
        ),
    ]
