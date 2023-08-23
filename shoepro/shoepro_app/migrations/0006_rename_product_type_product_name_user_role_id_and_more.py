# Generated by Django 4.2.4 on 2023-08-23 10:52

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('shoepro_app', '0005_alter_producttaxonomyterm_ptt_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_type',
            new_name='name',
        ),
        migrations.AddField(
            model_name='user',
            name='role_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shoepro_app.role'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]