# Generated by Django 5.0.6 on 2024-07-03 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=255)),
                ('phone', models.TextField(verbose_name=13)),
                ('email', models.EmailField(max_length=254)),
                ('messege', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Creative_work',
        ),
    ]