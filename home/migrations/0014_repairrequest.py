# Generated by Django 5.1.1 on 2024-10-21 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_faq'),
    ]

    operations = [
        migrations.CreateModel(
            name='RepairRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(choices=[('iphone', 'iPhone'), ('samsung', 'Samsung'), ('lg', 'LG'), ('google', 'Google'), ('motorola', 'Motorola'), ('other', 'Other')], max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('problems', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
                ('service_method', models.CharField(max_length=20)),
                ('store_location', models.CharField(blank=True, max_length=100, null=True)),
                ('preferred_date', models.DateField(blank=True, null=True)),
                ('preferred_time', models.CharField(blank=True, max_length=20, null=True)),
                ('contact_first_name', models.CharField(max_length=50)),
                ('contact_last_name', models.CharField(max_length=50)),
                ('contact_email', models.EmailField(max_length=254)),
                ('contact_phone', models.CharField(max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]