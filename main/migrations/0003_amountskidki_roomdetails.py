# Generated by Django 4.2.7 on 2023-11-17 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_room_floor'),
    ]

    operations = [
        migrations.CreateModel(
            name='AmountSkidki',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.PositiveIntegerField(default=5)),
            ],
        ),
        migrations.CreateModel(
            name='RoomDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count_rooms', models.CharField(max_length=12)),
                ('full_area', models.FloatField(default=0)),
                ('terrace_area', models.FloatField(default=0)),
                ('image_1', models.ImageField(upload_to='images/')),
                ('image_2', models.ImageField(upload_to='images/')),
                ('client_name', models.CharField(blank=True, max_length=123, null=True)),
                ('price', models.PositiveIntegerField(default=0)),
                ('terrace_price', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
