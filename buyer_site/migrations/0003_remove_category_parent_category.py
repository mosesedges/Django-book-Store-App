# Generated by Django 3.2.7 on 2021-09-27 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buyer_site', '0002_auto_20210923_1433'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='parent_category',
        ),
    ]
