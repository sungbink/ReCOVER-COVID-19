# Generated by Django 3.0.4 on 2020-06-07 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('model_api', '0008_load_predictions'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuarantineScoreDataPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('val', models.FloatField()),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model_api.Area')),
            ],
        ),
    ]
