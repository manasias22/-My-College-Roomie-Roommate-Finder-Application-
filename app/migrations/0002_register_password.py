# Generated by Django 4.1.7 on 2023-03-31 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='password',
            field=models.TextField(default=0),
        ),
    ]