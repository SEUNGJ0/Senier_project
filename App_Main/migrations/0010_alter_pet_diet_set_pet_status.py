# Generated by Django 4.1.3 on 2022-11-16 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Main', '0009_remove_pet_diet_set_pet_breed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet_diet_set',
            name='pet_status',
            field=models.CharField(choices=[('성견__중성화', 'Adult_Neutering'), ('성견__미중성화', 'Adult_NonNeutering'), ('성견__비만경향', 'Adult_Obese_NonActive'), ('성견__활동적', 'Adult_Active'), ('성견__매우 활동적', 'Adult_Very_Active'), ('성견__체중감량', 'Adult_Wloss'), ('성견__체중증가', 'Adult_gain'), ('성견__아픔', 'Adult_Week'), ('성장기__생후 4개월 전', 'Growth_Ud4'), ('성장기__4개월 이후~ 성견 전', 'Growth_Up4'), ('임신 전반 6주', 'Pregent_6W'), ('임신 전반 3주', 'Pregent_3W'), ('수유 1마리', 'Nursing_1'), ('수유 2마리', 'Nursing_2'), ('수유 3~4마리', 'Nursing_3_4'), ('수유 5~6마리', 'Nursing_5_6'), ('수유 7~8마리', 'Nursing_7_8'), ('수유 9마리 이상', 'Nursing_9')], max_length=100, verbose_name='반려견 상태'),
        ),
    ]
