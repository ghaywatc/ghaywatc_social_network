# Generated by Django 3.1.1 on 2021-02-25 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='member',
            new_name='members',
        ),
    ]
