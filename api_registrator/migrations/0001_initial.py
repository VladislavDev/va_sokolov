# Generated by Django 3.2.9 on 2023-03-22 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApiRegistrator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_type', models.CharField(max_length=10)),
                ('request_date', models.DateTimeField(verbose_name='DateTime')),
                ('request_text', models.CharField(max_length=250)),
                ('response_status_code', models.IntegerField(default=0)),
                ('response_text', models.TextField()),
            ],
        ),
    ]
