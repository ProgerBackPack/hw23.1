# Generated by Django 5.1 on 2024-09-02 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='manufactured_at',
            field=models.DateField(blank=True, help_text='Введите дату производства продукта нашего', null=True, verbose_name='Дата производства продукта нашего'),
        ),
    ]
