# Generated by Django 4.2 on 2023-05-03 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_share', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to=None),
        ),
    ]
