# Generated by Django 4.1.4 on 2022-12-23 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelapp', '0003_alter_bookmodel_genera'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmodel',
            name='genera',
            field=models.CharField(choices=[['Drama', 'Drama'], ['crime', 'crime'], ['thriller', 'thriller'], ['biography', 'biography']], default='none', max_length=50),
        ),
    ]