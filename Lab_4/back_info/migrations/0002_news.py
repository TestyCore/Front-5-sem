# Generated by Django 4.2.1 on 2023-09-14 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back_info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('content', models.CharField(max_length=1000)),
                ('img_path', models.CharField(max_length=200)),
            ],
        ),
    ]