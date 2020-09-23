# Generated by Django 2.2.7 on 2020-09-11 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='location',
            new_name='address',
        ),
        migrations.AddField(
            model_name='profile',
            name='cart',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='coupons',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='number',
            field=models.IntegerField(default=99),
        ),
        migrations.AddField(
            model_name='profile',
            name='wishlist',
            field=models.CharField(default=' ', max_length=500),
        ),
    ]
