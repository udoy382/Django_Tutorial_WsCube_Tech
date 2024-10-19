# Generated by Django 4.2.2 on 2023-07-09 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Forms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('user_address', models.CharField(max_length=100)),
                ('user_number', models.CharField(max_length=14)),
                ('user_email', models.EmailField(max_length=254)),
                ('user_password', models.CharField(max_length=100)),
            ],
        ),
    ]