# Generated by Django 5.1.1 on 2024-09-30 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_materialentry_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='materialentry',
            name='rating',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
