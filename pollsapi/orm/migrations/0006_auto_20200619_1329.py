# Generated by Django 3.0.7 on 2020-06-19 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0005_origin'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.RemoveField(
            model_name='hero',
            name='benevolence_factor',
        ),
        migrations.AddField(
            model_name='category',
            name='hero_count',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='category',
            name='villian_count',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Villian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orm.Category')),
            ],
        ),
    ]