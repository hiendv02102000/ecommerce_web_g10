# Generated by Django 4.0.3 on 2022-04-11 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_bookauthor_itembook_book_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageBook',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('src', models.CharField(max_length=255)),
            ],
        ),
    ]