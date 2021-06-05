# Generated by Django 2.2.7 on 2019-11-27 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0007_auto_20191127_0352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='manager',
        ),
        migrations.AddField(
            model_name='employee',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee', to='employee.Employee'),
        ),
    ]
