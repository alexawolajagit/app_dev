# Generated by Django 4.2.4 on 2023-08-23 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoepro_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lineitems',
            name='PK',
        ),
        migrations.RemoveField(
            model_name='notifications',
            name='PK',
        ),
        migrations.RemoveField(
            model_name='ordernotes',
            name='PK',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='PK',
        ),
        migrations.RemoveField(
            model_name='pages',
            name='PK',
        ),
        migrations.RemoveField(
            model_name='products',
            name='PK',
        ),
        migrations.RemoveField(
            model_name='producttaxonomies',
            name='PK',
        ),
        migrations.RemoveField(
            model_name='producttaxonomyterms',
            name='PK',
        ),
        migrations.RemoveField(
            model_name='productterms',
            name='PK',
        ),
        migrations.RemoveField(
            model_name='roles',
            name='PK',
        ),
        migrations.RemoveField(
            model_name='settings',
            name='PK',
        ),
        migrations.RemoveField(
            model_name='users',
            name='PK',
        ),
    ]
