# Generated by Django 5.1.7 on 2025-04-09 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateField()),
                ('phno', models.IntegerField()),
                ('addr', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
