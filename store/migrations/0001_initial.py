# Generated by Django 2.1.4 on 2019-01-03 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter product name', max_length=200)),
                ('description', models.TextField(help_text='Enter product description')),
                ('price', models.DecimalField(decimal_places=2, help_text='Enter product price', max_digits=8)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
