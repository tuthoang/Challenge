# Generated by Django 4.2.3 on 2023-07-15 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageDetail',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('views', models.IntegerField()),
                ('downloads', models.IntegerField()),
                ('likes', models.IntegerField()),
                ('comments', models.IntegerField()),
                ('user', models.CharField(max_length=50)),
                ('tags', models.CharField(max_length=200)),
                ('previewURL', models.CharField(max_length=200)),
                ('webformatURL', models.CharField(max_length=200)),
            ],
        ),
    ]