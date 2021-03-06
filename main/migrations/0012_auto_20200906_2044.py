# Generated by Django 3.1.1 on 2020-09-07 01:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_timeavailabilitymodel_day2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timeavailabilitymodel',
            name='day2',
        ),
        migrations.AddField(
            model_name='timeavailabilitymodel',
            name='num_end_day',
            field=models.CharField(blank=True, choices=[('1', 'Lunes'), ('2', 'Martes'), ('3', 'Miércoles'), ('4', 'Jueves'), ('5', 'Viernes'), ('6', 'Sábado'), ('7', 'Domingo')], default='1', help_text='Segundo día. Ej: Jueves.', max_length=5, null=True, verbose_name='Día 2'),
        ),
        migrations.AddField(
            model_name='timeavailabilitymodel',
            name='num_start_day',
            field=models.CharField(choices=[('1', 'Lunes'), ('2', 'Martes'), ('3', 'Miércoles'), ('4', 'Jueves'), ('5', 'Viernes'), ('6', 'Sábado'), ('7', 'Domingo')], default='1', help_text='Día inicial. Ej: Lunes.', max_length=5, verbose_name='Día 1'),
        ),
        migrations.AlterField(
            model_name='timeavailabilitymodel',
            name='day',
            field=models.DateField(blank=True, help_text='Fecha disponibilidad', null=True, verbose_name='Día'),
        ),
        migrations.AlterField(
            model_name='timeavailabilitymodel',
            name='teachers',
            field=models.ForeignKey(help_text='Seleccione profesor', on_delete=django.db.models.deletion.CASCADE, related_name='availabilities', to='main.teachermodel', verbose_name='Profesor'),
        ),
    ]
