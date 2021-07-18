# Generated by Django 4.0.dev20210521113437 on 2021-07-04 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0004_alter_operation_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='operation_name',
            field=models.CharField(choices=[('1 forming', 'Forming'), ('2 trimming', 'Trimming'), ('3 chemi-clean', 'Chemi-Clean'), ('4 re-strike', 'Re-Strike'), ('5 goods-In_Inspection', 'Goods-in Inspection'), ('6 pre-Assembly', 'Pre-Assembly'), ('7 assembly', 'Assembly'), ('8 hemming', 'Hemming'), ('9 a-Class', 'A-Class'), ('10 gap_and_flush', 'Gap and Flush'), ('11 heat_treatment', 'Heat Treatment'), ('12 final_inspection', 'Final Inspection')], max_length=120),
        ),
    ]
