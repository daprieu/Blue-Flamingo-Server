# Generated by Django 3.2.4 on 2021-06-14 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blueflamingoapi', '0003_rename_hardness_notes_pumphouseparameters_hardness_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pumphouseparameters',
            name='hardness',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='blueflamingoapi.hardness'),
        ),
    ]