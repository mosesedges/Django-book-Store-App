# Generated by Django 3.2.7 on 2021-09-23 13:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('buyer_site', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ('-posted_on',), 'verbose_name': 'Book', 'verbose_name_plural': 'Books'},
        ),
        migrations.AddField(
            model_name='book',
            name='posted_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='buyer_site.category'),
        ),
    ]
