# Generated by Django 2.2.24 on 2021-06-20 18:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testspackages', '0002_filefield'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testspackage',
            name='name',
            field=models.CharField(help_text='File name can only contain letters, digits, - and _. It should not contain file extension such as .zip, .tgz, etc.', max_length=30, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z\\-_]+$', 'Name can only contain letters, digits, - and _.')], verbose_name='file name'),
        ),
    ]
