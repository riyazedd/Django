# Generated by Django 4.1.5 on 2023-01-31 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_categories'),
    ]

    operations = [
        migrations.DeleteModel(
            name='categories',
        ),
    ]
