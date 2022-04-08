# Generated by Django 4.0 on 2022-04-08 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_rename_categorybookid_book_categorybook_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookAuthor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('bio', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ItemBook',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.FloatField(null=True)),
                ('discount', models.FloatField(null=True)),
                ('promo_text', models.CharField(max_length=255)),
                ('decription', models.CharField(max_length=255)),
                ('inventory', models.CharField(max_length=255)),
                ('is_for_sale', models.BooleanField(default=True)),
                ('Book', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='book.book')),
            ],
        ),
        migrations.CreateModel(
            name='Book_Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='book.bookauthor')),
                ('Book', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='book.book')),
            ],
        ),
    ]