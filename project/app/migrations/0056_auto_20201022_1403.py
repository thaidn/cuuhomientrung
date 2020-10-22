# Generated by Django 3.1.2 on 2020-10-22 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0055_historicalhodan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuuho',
            name='huyen',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cuuho_reversed', to='app.huyen'),
        ),
        migrations.AlterField(
            model_name='cuuho',
            name='thon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cuuho_reversed', to='app.thon'),
        ),
        migrations.AlterField(
            model_name='cuuho',
            name='xa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cuuho_reversed', to='app.xa'),
        ),
    ]