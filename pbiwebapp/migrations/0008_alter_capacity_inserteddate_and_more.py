# Generated by Django 5.0.1 on 2024-01-04 17:13

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pbiwebapp', '0007_alter_capacity_inserteddate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capacity',
            name='insertedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 17, 13, 34, 746957, tzinfo=datetime.timezone.utc), verbose_name='Created at:'),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='insertedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 17, 13, 34, 747958, tzinfo=datetime.timezone.utc), verbose_name='Created at:'),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='workspaceId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pbiwebapp.workspace'),
        ),
        migrations.AlterField(
            model_name='powerbi_setting',
            name='insertedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 17, 13, 34, 695025, tzinfo=datetime.timezone.utc), verbose_name='Created at:'),
        ),
        migrations.AlterField(
            model_name='workspace',
            name='capacityId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pbiwebapp.capacity'),
        ),
        migrations.AlterField(
            model_name='workspace',
            name='insertedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 17, 13, 34, 747958, tzinfo=datetime.timezone.utc), verbose_name='Created at:'),
        ),
    ]
