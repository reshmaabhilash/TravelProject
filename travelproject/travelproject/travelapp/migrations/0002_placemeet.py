# Generated by Django 4.0.5 on 2022-07-04 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Placemeet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=250)),
                ('img2', models.ImageField(upload_to='pics')),
                ('desc2', models.TextField()),
            ],
        ),
    ]
