# Generated by Django 2.2.7 on 2019-11-25 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20191115_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='worksite',
            name='contact_info',
            field=models.CharField(max_length=200, null=True),
        ),
    ]