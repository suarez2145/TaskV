# Generated by Django 2.2.7 on 2019-11-25 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_worksite_contact_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='worksite',
            name='codes_notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
