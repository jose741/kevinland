# Generated by Django 2.2.5 on 2019-10-17 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='tipo',
            field=models.CharField(default='perro', max_length=50),
            preserve_default=False,
        ),
    ]
