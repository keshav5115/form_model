# Generated by Django 4.1.4 on 2022-12-23 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmodel',
            fields=[
                ('book_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('book_name', models.CharField(max_length=40)),
                ('author_name', models.CharField(max_length=30)),
                ('publication', models.CharField(max_length=40)),
                ('Release_date', models.DateField()),
                ('genera', models.CharField(choices=[['Drama', 'Drama'], ['crime', 'crime'], ['thriller', 'thriller'], ['biography', 'biography']], max_length=15)),
                ('price', models.PositiveIntegerField()),
            ],
        ),
    ]
