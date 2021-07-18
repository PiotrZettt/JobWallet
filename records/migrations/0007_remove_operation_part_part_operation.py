# Generated by Django 4.0.dev20210521113437 on 2021-07-09 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0006_remove_part_operation_operation_part'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operation',
            name='part',
        ),
        migrations.AddField(
            model_name='part',
            name='operation',
            field=models.ManyToManyField(help_text='Select an operation for this part', to='records.Operation'),
        ),
    ]
