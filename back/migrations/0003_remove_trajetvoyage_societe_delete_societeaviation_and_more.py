# Generated by Django 4.2.3 on 2023-11-21 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0002_societeaviation_trajetvoyage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trajetvoyage',
            name='societe',
        ),
        migrations.DeleteModel(
            name='SocieteAviation',
        ),
        migrations.DeleteModel(
            name='TrajetVoyage',
        ),
    ]
