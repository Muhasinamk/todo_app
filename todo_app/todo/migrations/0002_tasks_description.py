# Generated by Django 4.1.5 on 2023-02-09 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
