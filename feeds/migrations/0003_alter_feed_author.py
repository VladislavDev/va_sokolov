# Generated by Django 3.2.9 on 2023-03-24 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_profile_location'),
        ('feeds', '0002_auto_20230324_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userprofile.profile'),
        ),
    ]
