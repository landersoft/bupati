# Generated by Django 2.2.2 on 2019-08-08 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0007_auto_20190808_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='comentario',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='fecha_derivacion',
            field=models.DateField(blank=True, null=True),
        ),
    ]
