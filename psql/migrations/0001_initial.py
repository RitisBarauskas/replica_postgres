# Generated by Django 3.2.7 on 2021-09-29 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=50, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'worker',
                'verbose_name_plural': 'workers',
            },
        ),
    ]