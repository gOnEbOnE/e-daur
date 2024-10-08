# Generated by Django 5.1.1 on 2024-09-17 11:05

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_product_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaterialEntry',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('material', models.CharField(max_length=255)),
                ('item', models.CharField(max_length=255)),
                ('material_quantity', models.IntegerField()),
                ('item_quantity', models.IntegerField()),
                ('notes', models.TextField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
