# Generated by Django 2.2.7 on 2019-11-17 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_controller', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]