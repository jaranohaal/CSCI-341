# Generated by Django 3.2.16 on 2022-11-20 01:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20221120_0653'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discover',
            fields=[
                ('cname', models.OneToOneField(db_column='cname', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='users.country')),
                ('first_enc_date', models.DateField()),
            ],
            options={
                'db_table': 'Discover',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('disease_code', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('pathogen', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=140)),
            ],
            options={
                'db_table': 'Disease',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Specialize',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='users.diseasetype')),
            ],
            options={
                'db_table': 'Specialize',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('email', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=40)),
                ('salary', models.IntegerField()),
                ('phone', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Users',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='diseasetype',
            options={'managed': False},
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('email', models.OneToOneField(db_column='email', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='users.users')),
                ('degree', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Doctor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PublicServant',
            fields=[
                ('email', models.OneToOneField(db_column='email', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='users.users')),
                ('department', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Public servant',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('email', models.OneToOneField(db_column='email', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='users.publicservant')),
                ('total_deaths', models.IntegerField()),
                ('total_patients', models.IntegerField()),
            ],
            options={
                'db_table': 'Record',
                'managed': False,
            },
        ),
    ]
