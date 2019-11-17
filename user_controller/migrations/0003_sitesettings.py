# Generated by Django 2.2.7 on 2019-11-17 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_controller', '0002_auto_20191117_0637'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='AdefemiGreat', max_length=50)),
                ('picture', models.TextField()),
                ('about', models.TextField()),
                ('resume', models.TextField()),
                ('copyright', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]