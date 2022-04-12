# Generated by Django 4.0 on 2022-04-12 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryMobilePhone',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MobilePhone',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('manufacturer_date', models.DateField()),
                ('weight', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
                ('warranty', models.CharField(max_length=255)),
                ('dimensions', models.CharField(max_length=255)),
                ('countryOrigin', models.CharField(max_length=255)),
                ('cpu', models.CharField(max_length=255)),
                ('gpu', models.CharField(max_length=255)),
                ('storageSize', models.CharField(max_length=255)),
                ('screenSize', models.CharField(max_length=255)),
                ('screenResolution', models.CharField(max_length=255)),
                ('ramSize', models.CharField(max_length=255)),
                ('ramType', models.CharField(max_length=255)),
                ('connections', models.CharField(max_length=255)),
                ('interfaces', models.CharField(max_length=255)),
                ('battery', models.CharField(max_length=255)),
                ('os', models.CharField(max_length=255)),
                ('speaker', models.CharField(max_length=255)),
                ('frontCamera', models.CharField(max_length=255)),
                ('rearCamera', models.CharField(max_length=255)),
                ('CategoryMobilePhone', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mobile_phone.categorymobilephone')),
            ],
        ),
        migrations.CreateModel(
            name='ItemMobilePhone',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.FloatField(null=True)),
                ('discount', models.FloatField(null=True)),
                ('promoText', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('inventory', models.CharField(max_length=255)),
                ('is_for_sale', models.BooleanField(default=True)),
                ('mobilePhone', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mobile_phone.mobilephone')),
            ],
        ),
    ]
