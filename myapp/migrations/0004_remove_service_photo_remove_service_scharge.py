# Generated by Django 4.1.7 on 2023-03-02 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_member_cpw_member_fname_member_phone_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='service',
            name='scharge',
        ),
    ]