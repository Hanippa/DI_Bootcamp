# Generated by Django 4.2.1 on 2023-05-08 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_rename_tasks_task_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='department_administrator',
            field=models.BooleanField(default=False),
        ),
    ]
