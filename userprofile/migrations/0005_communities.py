# Generated by Django 3.2.9 on 2023-04-17 17:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userprofile', '0004_auto_20230410_1557'),
    ]

    operations = [
        migrations.CreateModel(
            name='Communities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community_type', models.CharField(choices=[('so', 'stackoverflow'), ('gh', 'GitHub')], max_length=7)),
                ('identifier', models.CharField(max_length=30)),
                ('use_personal', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='communities', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]