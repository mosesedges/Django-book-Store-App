# Generated by Django 3.2.7 on 2021-09-29 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyer_site', '0008_auto_20210929_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='book_id',
            field=models.BigIntegerField(default=1),
        ),
    ]
