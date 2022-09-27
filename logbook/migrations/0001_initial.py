# Generated by Django 3.2.13 on 2022-09-27 17:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('date', models.DateField()),
                ('location', models.CharField(max_length=255)),
                ('diving_site', models.CharField(max_length=255)),
                ('duration', models.CharField(max_length=255)),
                ('depth', models.CharField(max_length=255)),
                ('gas_mixture', models.CharField(max_length=255)),
                ('air_in', models.CharField(max_length=255)),
                ('air_out', models.CharField(max_length=255)),
                ('visibility', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dive_name', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
