# Generated by Django 5.2 on 2025-05-16 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_ethnic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Western',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='imagess')),
                ('price', models.FloatField()),
            ],
        ),
    ]
