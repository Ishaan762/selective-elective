# Generated by Django 3.2.23 on 2023-11-09 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20231109_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='SRN',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]
