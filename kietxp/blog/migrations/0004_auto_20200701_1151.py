# Generated by Django 3.0.5 on 2020-07-01 11:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200430_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Phone_number',
            field=models.CharField(default=6666666666, max_length=10, validators=[django.core.validators.RegexValidator(code='Invalid', message='Invalid mobile number entered', regex='^[6789][0-9]{9}$')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('BOOKS', 'BOOKS'), ('LAB ACCESSORIES', 'LAB ACCESSORIES'), ('ELECTRONICS', 'ELECTRONICS'), ('OTHERS', 'OTHERS')], default='', max_length=20),
        ),
    ]
