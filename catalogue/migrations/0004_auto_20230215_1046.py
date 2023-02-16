# Generated by Django 3.2.17 on 2023-02-15 07:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0003_alter_bookinstance_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='summary',
            field=models.TextField(help_text='Brief Description', max_length=250),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='id',
            field=models.UUIDField(default=uuid.UUID('45229a3b-a587-40cb-80fe-75b80b8cfa3d'), help_text='unique ID', primary_key=True, serialize=False),
        ),
    ]
