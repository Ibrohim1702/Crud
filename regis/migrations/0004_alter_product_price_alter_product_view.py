# Generated by Django 4.2 on 2023-04-29 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regis', '0003_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='view',
            field=models.IntegerField(default=0),
        ),
    ]