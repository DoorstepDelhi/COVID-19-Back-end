# Generated by Django 3.2.3 on 2021-05-17 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='hindi_name',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
