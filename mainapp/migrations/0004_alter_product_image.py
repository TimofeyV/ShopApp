# Generated by Django 5.0.6 on 2024-05-10 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='products/', verbose_name='Изображение товара'),
        ),
    ]
