# Generated by Django 3.0.7 on 2020-06-15 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mode', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_date',
            field=models.DateField(auto_now=True),
        ),
    ]
