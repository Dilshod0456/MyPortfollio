# Generated by Django 4.0.3 on 2022-07-19 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Xabarlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fish', models.CharField(max_length=250)),
                ('tell', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=254)),
                ('text', models.TimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='loyihalar',
            name='discription',
            field=models.CharField(max_length=200),
        ),
    ]
