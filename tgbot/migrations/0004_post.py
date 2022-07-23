# Generated by Django 4.0.6 on 2022-07-22 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tgbot', '0003_rm_unused_fields'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Nomi')),
                ('content', models.TextField()),
                ('image', models.URLField()),
            ],
        ),
    ]
