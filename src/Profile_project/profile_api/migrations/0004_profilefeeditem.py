# Generated by Django 4.0.1 on 2022-04-18 03:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile_api', '0003_userprofile_delete_myuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileFeedItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_text', models.CharField(max_length=225)),
                ('create_on', models.DateTimeField(auto_now_add=True)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
