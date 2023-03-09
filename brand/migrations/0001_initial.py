# Generated by Django 4.1.7 on 2023-03-09 05:54

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brandname', models.CharField(max_length=100, verbose_name='Brand name')),
                ('brandlogo', models.ImageField(blank=True, upload_to='images/')),
                ('saytlink', models.URLField(blank=True, db_index=True, max_length=128, unique=True, verbose_name='Sayt link')),
                ('brandinfo', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Brandimages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='brandimages', to='brand.brand')),
            ],
        ),
    ]