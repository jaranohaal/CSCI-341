# Generated by Django 3.2.16 on 2022-11-20 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('cname', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('population', models.BigIntegerField()),
            ],
        ),
    ]
