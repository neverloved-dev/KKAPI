# Generated by Django 4.1.1 on 2022-09-27 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='url',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(default='password', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='password',
            field=models.CharField(default='password', max_length=500),
            preserve_default=False,
        ),
    ]