# Generated by Django 4.0.1 on 2022-02-04 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='maturity_setting',
            field=models.CharField(choices=[('all', 'All'), ('kids', 'kids')], max_length=50),
        ),
    ]
