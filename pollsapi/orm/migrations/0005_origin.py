# Generated by Django 3.0.7 on 2020-06-19 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0004_category_hero'),
    ]

    operations = [
        migrations.CreateModel(
            name='Origin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]