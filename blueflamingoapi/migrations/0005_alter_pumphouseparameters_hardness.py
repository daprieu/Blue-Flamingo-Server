# Generated by Django 3.2.4 on 2021-06-14 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blueflamingoapi', '0004_alter_pumphouseparameters_hardness'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pumphouseparameters',
            name='hardness',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blueflamingoapi.hardness'),
        ),
    ]