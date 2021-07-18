# Generated by Django 4.0.dev20210521113437 on 2021-07-09 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0005_alter_operation_operation_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='part',
            name='operation',
        ),
        migrations.AddField(
            model_name='operation',
            name='part',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='records.part'),
        ),
    ]
