# Generated by Django 2.2.12 on 2021-02-10 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guest_post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('datetime', models.DateTimeField(verbose_name='Дата публикции')),
                ('content', models.TextField(max_length=100000)),
            ],
        ),
        migrations.CreateModel(
            name='Lib_post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('datetime', models.DateTimeField(verbose_name='Дата публикции')),
                ('content', models.TextField(max_length=100000)),
            ],
        ),
        migrations.CreateModel(
            name='Media_post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('datetime', models.DateTimeField(verbose_name='Дата публикции')),
                ('content', models.TextField(max_length=100000)),
            ],
        ),
        migrations.CreateModel(
            name='News_post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('datetime', models.DateTimeField(verbose_name='Дата публикции')),
                ('content', models.TextField(max_length=100000)),
            ],
        ),
        migrations.RenameModel(
            old_name='Post',
            new_name='Chess_post',
        ),
    ]
