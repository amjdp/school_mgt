# Generated by Django 4.1.2 on 2022-10-24 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_rename_parent_name_student_s_parent_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
    ]