# Generated by Django 3.0.3 on 2020-03-06 15:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('patients', '0006_auto_20200307_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_by_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='patient',
            name='detected_location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='detected_location_loc', to='patients.PatientLocation'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modified_by_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='patient',
            name='residing_location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='residing_location_loc', to='patients.PatientLocation'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='patients.PatientStatus'),
        ),
    ]