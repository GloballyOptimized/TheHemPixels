# Generated by Django 4.1.5 on 2023-02-23 09:34

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('image_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='Portfolio_Data')),
                ('uploaded_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]