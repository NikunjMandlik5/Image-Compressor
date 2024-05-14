# Generated by Django 4.1.2 on 2022-10-26 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagecompressor', '0002_image_date_alter_image_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompressedImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='Compressed')),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
