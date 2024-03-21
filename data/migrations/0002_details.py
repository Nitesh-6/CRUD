# Generated by Django 5.0.3 on 2024-03-13 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('username', models.EmailField(max_length=254)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=30)),
                ('zipcode', models.IntegerField()),
            ],
        ),
    ]
