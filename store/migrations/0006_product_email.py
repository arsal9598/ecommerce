# Generated by Django 2.1.4 on 2019-01-05 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_product_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
