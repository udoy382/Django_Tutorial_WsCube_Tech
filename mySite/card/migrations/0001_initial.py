# Generated by Django 4.2.2 on 2023-07-06 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_title', models.CharField(max_length=50)),
                ('card_desc', models.TextField()),
                ('card_image', models.FileField(default=None, max_length=250, null=True, upload_to='cards/')),
            ],
        ),
    ]