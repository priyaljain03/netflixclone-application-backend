# Generated by Django 4.0.1 on 2022-02-10 09:35

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profile_maturity_setting'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profiles/default.png', upload_to=users.models.upload_to),
        ),
    ]
