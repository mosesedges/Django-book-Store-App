# Generated by Django 3.2.7 on 2021-09-29 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyer_site', '0011_alter_review_book_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='posted_on',
            field=models.DateTimeField(default=1),
        ),
    ]
