# Generated by Django 4.1.7 on 2023-04-24 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardno', models.CharField(max_length=20)),
                ('cardname', models.CharField(max_length=20)),
                ('expmonth', models.CharField(max_length=20)),
                ('expyear', models.CharField(max_length=20)),
                ('cvv', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='service',
            name='des',
            field=models.CharField(max_length=200, verbose_name='description'),
        ),
    ]