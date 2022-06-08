# Generated by Django 4.0.4 on 2022-05-11 08:55

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_alter_post_released_date_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='polls.person')),
                ('email', models.URLField()),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='released_date',
            field=models.DateField(default=datetime.datetime(2022, 5, 11, 8, 55, 19, 310369)),
        ),
    ]