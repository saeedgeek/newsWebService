# Generated by Django 2.2.6 on 2019-12-22 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('name', models.CharField(max_length=42, primary_key=True, serialize=False, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=400)),
                ('dt', models.DateField()),
                ('autor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Author')),
            ],
        ),
    ]
