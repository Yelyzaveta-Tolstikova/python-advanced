# Generated by Django 4.0.4 on 2022-04-21 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.CharField(db_index=True, max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.CharField(db_index=True, max_length=200, unique=True)),
                ('text', models.TextField()),
                ('date_published', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('publication_status', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.category')),
            ],
        ),
    ]
