# Generated by Django 3.2.4 on 2021-06-26 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sahitya',
            name='slug',
            field=models.CharField(default='', max_length=130),
            preserve_default=False,
        ),
    ]