# Generated by Django 3.2.9 on 2021-12-20 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0011_auto_20211219_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]