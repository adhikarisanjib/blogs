# Generated by Django 3.2 on 2022-04-27 03:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20220423_0913'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reply',
            options={'ordering': ['date_time'], 'verbose_name': 'Reply', 'verbose_name_plural': 'Replies'},
        ),
    ]
