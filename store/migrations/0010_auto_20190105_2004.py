# Generated by Django 2.1.4 on 2019-01-06 02:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20190105_2004'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-id']},
        ),
    ]
