# Generated by Django 2.2.7 on 2019-11-17 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_controller', '0003_sitesettings'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
