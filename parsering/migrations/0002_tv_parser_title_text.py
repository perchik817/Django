# Generated by Django 4.1.3 on 2022-12-01 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsering', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tv_parser',
            name='title_text',
            field=models.CharField(max_length=200, null=True),
        ),
    ]