# Generated by Django 4.2.1 on 2023-05-31 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solution', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='images/img1.jpg', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
    ]
