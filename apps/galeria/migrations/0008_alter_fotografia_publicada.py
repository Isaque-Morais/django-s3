# Generated by Django 4.1 on 2023-03-27 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0007_alter_fotografia_publicada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='publicada',
            field=models.BooleanField(default=False),
        ),
    ]
