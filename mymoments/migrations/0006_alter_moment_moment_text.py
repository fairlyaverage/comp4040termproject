# Generated by Django 4.1.2 on 2022-12-07 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymoments', '0005_alter_moment_moment_edited'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moment',
            name='moment_text',
            field=models.TextField(default='ici', help_text='Text body for a Moment'),
        ),
    ]