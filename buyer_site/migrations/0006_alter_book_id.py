# Generated by Django 3.2.7 on 2021-09-28 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyer_site', '0005_alter_book_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
