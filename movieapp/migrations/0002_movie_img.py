# Generated by Django 3.2.16 on 2022-10-25 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='asfcfg', upload_to='gallery'),
            preserve_default=False,
        ),
    ]