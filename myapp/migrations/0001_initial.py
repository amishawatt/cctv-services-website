# Generated by Django 4.1.7 on 2023-02-23 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=100, verbose_name='Service Name')),
                ('scharge', models.CharField(max_length=100, verbose_name='Service charge')),
                ('des', models.CharField(max_length=100, verbose_name='description')),
                ('photo', models.ImageField(upload_to='images/')),
                ('category', models.CharField(choices=[('CCTV INSTALLATION', 'CCTV INSTALLATION'), ('CCTV CONFIGURATION', 'CCTV CONFIGURATION'), ('CCTV MAINTENANCE', 'CCTV MAINTENANCE'), ('CCTV REPAIR & SERVICES', 'CCTV REPAIR & SERVICES'), ('CCTV MONITERING', 'CCTV MONITERING'), ('CCTV ACCESS CONTROL', 'CCTV ACCESS CONTROL')], max_length=100)),
            ],
        ),
    ]