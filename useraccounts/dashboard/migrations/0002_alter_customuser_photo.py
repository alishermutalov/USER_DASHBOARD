# Generated by Django 5.0.6 on 2024-05-26 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='photo',
            field=models.ImageField(upload_to='user/avatar/%Y/%m/%d', verbose_name='Photo'),
        ),
    ]
