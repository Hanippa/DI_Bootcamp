# Generated by Django 4.2 on 2023-04-30 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0003_alter_film_director'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='director',
            field=models.ManyToManyField(related_name='director_film', to='films.director'),
        ),
    ]