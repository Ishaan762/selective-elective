# Generated by Django 3.2.23 on 2023-11-09 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_alter_student_srn'),
    ]

    operations = [
        migrations.RenameField(
            model_name='elective',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='elective',
            name='last_name',
        ),
    ]
