# Generated by Django 2.2.7 on 2019-11-18 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levels', '0002_auto_20191118_1015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flags',
            name='id',
        ),
        migrations.AddField(
            model_name='flags',
            name='flagID',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flags',
            name='flagString',
            field=models.CharField(default='-', max_length=50),
        ),
    ]
