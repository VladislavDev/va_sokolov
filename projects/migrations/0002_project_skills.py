# Generated by Django 3.2.9 on 2023-02-24 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0002_auto_20230224_1623'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='skills',
            field=models.ManyToManyField(to='skills.HardSkill'),
        ),
    ]
