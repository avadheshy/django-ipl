# Generated by Django 4.0.5 on 2022-07-08 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0003_alter_deliveries_match_id_alter_matches_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveries',
            name='match_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='match.matches'),
        ),
    ]
