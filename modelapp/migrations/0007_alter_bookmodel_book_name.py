# Generated by Django 4.1.4 on 2022-12-23 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelapp', '0006_alter_bookmodel_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmodel',
            name='book_name',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
