# Generated by Django 4.2.9 on 2024-01-16 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='datainsert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='x', max_length=200)),
                ('title', models.CharField(default='x', max_length=200)),
                ('play', models.CharField(default='x', max_length=200)),
            ],
        ),
    ]
