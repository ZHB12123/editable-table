# Generated by Django 2.2.1 on 2020-10-25 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Editable', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='microserviceinfo',
            old_name='Dev',
            new_name='dev',
        ),
    ]
