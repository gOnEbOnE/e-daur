# Generated by Django 5.1.1 on 2024-09-18 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_materialentry_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='materialentry',
            old_name='notes',
            new_name='deskripsi',
        ),
        migrations.RenameField(
            model_name='materialentry',
            old_name='item_quantity',
            new_name='harga',
        ),
        migrations.RenameField(
            model_name='materialentry',
            old_name='item',
            new_name='nama',
        ),
        migrations.RemoveField(
            model_name='materialentry',
            name='material',
        ),
        migrations.RemoveField(
            model_name='materialentry',
            name='material_quantity',
        ),
    ]
