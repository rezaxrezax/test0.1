# Generated by Django 2.2.6 on 2019-12-13 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20191213_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_text',
            field=models.TextField(verbose_name='comment'),
        ),
    ]
