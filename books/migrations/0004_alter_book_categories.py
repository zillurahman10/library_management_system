# Generated by Django 5.0.6 on 2024-06-16 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_category_remove_book_categories_book_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='categories',
            field=models.ManyToManyField(to='books.category'),
        ),
    ]
