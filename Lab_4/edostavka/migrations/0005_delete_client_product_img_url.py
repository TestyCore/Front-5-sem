# Generated by Django 4.2.1 on 2023-09-10 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edostavka', '0004_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img_url',
            field=models.CharField(default='root', max_length=100),
        ),
    ]