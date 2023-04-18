# Generated by Django 3.2.9 on 2023-04-09 17:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userprofile', '0002_profile_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_type', models.CharField(choices=[('mail', 'Email'), ('phone', 'Phone'), ('address', 'Address'), ('t.me', 'Telegram'), ('vk', 'VK')], max_length=7)),
                ('is_active', models.BooleanField(default=True)),
                ('contact', models.CharField(blank=True, max_length=40, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]