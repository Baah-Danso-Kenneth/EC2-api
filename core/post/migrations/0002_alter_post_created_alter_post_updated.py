# Generated by Django 4.0 on 2024-01-10 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]