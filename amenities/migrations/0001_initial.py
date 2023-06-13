# Generated by Django 4.2.1 on 2023-06-13 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amenities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]