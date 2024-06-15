# Generated by Django 5.0.6 on 2024-06-14 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='categories',
            field=models.CharField(blank=True, choices=[('Sci-Fi', 'Sci-Fi'), ('Fantasy', 'Fantasy'), ('Horror', 'Horror'), ('Romance', 'Romance'), ('Mystery', 'Mystery'), ('Thriller', 'Thriller'), ('Comedy', 'Comedy'), ('Action', 'Action'), ('Drama', 'Drama'), ('Crime', 'Crime'), ('Biography', 'Biography'), ('History', 'History'), ('Self-Help', 'Self-Help'), ('Health', 'Health'), ('Cooking', 'Cooking'), ('Education', 'Education'), ('Science', 'Science'), ('Poetry', 'Poetry'), ('Politics', 'Politics'), ('Business', 'Business'), ('Christian', 'Christian'), ('Womens-Fiction', 'Womens-Fiction'), ('Religion', 'Religion'), ('Spirituality', 'Spirituality'), ('Parenting', 'Parenting'), ('Travel', 'Travel')], max_length=20, null=True),
        ),
    ]