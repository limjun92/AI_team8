# Generated by Django 3.1.1 on 2020-10-05 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('prod_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('link', models.URLField()),
                ('gender', models.CharField(max_length=10)),
                ('category', models.CharField(max_length=10)),
                ('image', models.URLField()),
                ('brand', models.CharField(max_length=10)),
                ('price', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Similarity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_prod', models.CharField(max_length=10)),
                ('sim_prod', models.CharField(max_length=10)),
                ('similarity', models.FloatField()),
            ],
        ),
    ]
