# Generated by Django 2.2.10 on 2021-01-09 01:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryA',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('catagery_name', models.CharField(choices=[('mobile', 'MOBILE'), ('laptop', 'LAPTOP'), ('tv', 'TV'), ('desktop', 'DESKTOP'), ('computer', 'COMPUTER')], default='---', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('itemname', models.CharField(max_length=100)),
                ('cat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='items.CategoryA')),
            ],
        ),
    ]
