# Generated by Django 3.2 on 2021-04-27 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Foto')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('paragraph', models.TextField(verbose_name='Text')),
            ],
        ),
    ]
