# Generated by Django 4.0.dev20210521113437 on 2021-07-04 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0003_remove_operation_part_remove_part_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='operation',
            options={'ordering': ['operation_name']},
        ),
        migrations.AlterField(
            model_name='operation',
            name='operation_name',
            field=models.CharField(choices=[('1_forming', 'Forming'), ('2_trimming', 'Trimming'), ('3_chemi-clean', 'Chemi-Clean'), ('4_re-strike', 'Re-Strike'), ('5_goods-In_Inspection', 'Goods-in Inspection'), ('6_pre-Assembly', 'Pre-Assembly'), ('7_assembly', 'Assembly'), ('8_hemming', 'Hemming'), ('9_a-Class', 'A-Class'), ('10_gap_and_flush', 'Gap and Flush'), ('11_heat_treatment', 'Heat Treatment'), ('12_final_inspection', 'Final Inspection')], max_length=120),
        ),
    ]