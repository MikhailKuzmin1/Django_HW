# Generated by Django 4.2.7 on 2023-12-07 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HW02app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
