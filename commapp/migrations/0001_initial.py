# Generated by Django 5.1.2 on 2024-10-30 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('description', models.TextField()),
                ('composition', models.TextField(default='')),
                ('prodapp', models.TextField(default='')),
                ('category', models.ImageField(choices=[('CR', 'Crud'), ('ML', 'Milk'), ('LS', 'Lassi'), ('MS', 'MilkShake'), ('PN', 'Paneer'), ('GH', 'Ghee'), ('CZ', 'Cheese'), ('IC', 'ice-Cream')], max_length=2, upload_to='')),
                ('product_image', models.ImageField(upload_to='product')),
            ],
        ),
    ]