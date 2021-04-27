# Generated by Django 3.2 on 2021-04-27 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20210427_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioModal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('para1', models.TextField(verbose_name='Paragraph 1')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('para2', models.TextField(verbose_name='Paragraph 2')),
                ('date', models.DateField(verbose_name='Date')),
                ('client', models.CharField(max_length=100, verbose_name='Client')),
                ('category', models.CharField(max_length=100, verbose_name='Category')),
                ('portfolio', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='portfolio', to='home.portfolio')),
            ],
        ),
    ]
