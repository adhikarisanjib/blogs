# Generated by Django 3.2 on 2022-04-29 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_delete_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.CharField(choices=[('0', 'draft'), ('1', 'published')], default='0', max_length=16, verbose_name='Blog Status'),
        ),
    ]
