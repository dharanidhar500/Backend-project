# Generated by Django 4.1.2 on 2022-10-15 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0007_complaint_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='reported_by',
            field=models.CharField(default='username', max_length=20),
        ),
    ]