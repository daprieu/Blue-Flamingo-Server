# Generated by Django 3.2.4 on 2021-06-14 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blueflamingoapi', '0005_alter_pumphouseparameters_hardness'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pumphouseparameters',
            name='alkalinity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blueflamingoapi.alkalinity'),
        ),
        migrations.AlterField(
            model_name='pumphouseparameters',
            name='cyanuric_acid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blueflamingoapi.cyanuricacid'),
        ),
        migrations.AlterField(
            model_name='pumphouseparameters',
            name='filter_pressure',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blueflamingoapi.filterpressure'),
        ),
        migrations.AlterField(
            model_name='pumphouseparameters',
            name='free_chlorine',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blueflamingoapi.freechlorine'),
        ),
        migrations.AlterField(
            model_name='pumphouseparameters',
            name='ph',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blueflamingoapi.ph'),
        ),
        migrations.AlterField(
            model_name='pumphouseparameters',
            name='salinity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blueflamingoapi.salinity'),
        ),
        migrations.AlterField(
            model_name='pumphouseparameters',
            name='total_chlorine',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blueflamingoapi.totalchlorine'),
        ),
    ]
