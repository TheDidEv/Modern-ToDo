# Generated by Django 5.1 on 2024-08-30 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskcollection', '0003_taskstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskstatus',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
