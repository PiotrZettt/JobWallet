# Generated by Django 4.0.dev20210521113437 on 2021-07-03 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer',
            field=models.CharField(choices=[('McLaren', 'McLaren'), ('Ferrari', 'Ferrari'), ('Morgan', 'Morgan'), ('Maserati', 'Maserati')], default='Customer', max_length=120),
        ),
    ]
