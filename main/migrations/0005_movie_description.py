# Generated by Django 2.1.5 on 2021-04-27 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='description',
            field=models.CharField(default=None, max_length=1000, null=True),
        ),
    ]