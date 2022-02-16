# Generated by Django 4.0.2 on 2022-02-12 17:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('created', models.DateField(auto_now=True, verbose_name='Created')),
                ('updated', models.DateField(auto_now=True, verbose_name='Updated')),
                ('phone', models.CharField(blank=True, max_length=100, null=True, verbose_name='Phone')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Updated By')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Updated By')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Patient Abstract Class',
            },
        ),
        migrations.CreateModel(
            name='Especiality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('created', models.DateField(auto_now=True, verbose_name='Created')),
                ('updated', models.DateField(auto_now=True, verbose_name='Updated')),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Updated By')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Updated By')),
            ],
            options={
                'verbose_name': 'Doctor Abstract Class',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('created', models.DateField(auto_now=True, verbose_name='Created')),
                ('updated', models.DateField(auto_now=True, verbose_name='Updated')),
                ('phone', models.CharField(blank=True, max_length=100, null=True, verbose_name='Phone')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Updated By')),
                ('especiality', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.especiality', verbose_name='Especiality')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Updated By')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Doctor Abstract Class',
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('created', models.DateField(auto_now=True, verbose_name='Created')),
                ('updated', models.DateField(auto_now=True, verbose_name='Updated')),
                ('state', models.CharField(choices=[('REQUESTED', 'SOLICITADA'), ('REJECTED', 'RECHAZADA'), ('ACCEPTED', 'ACEPTADA')], default='REQUESTED', max_length=25, verbose_name='State')),
                ('due_date', models.DateField(verbose_name='Due date')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Updated By')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.doctor', verbose_name='Doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.patient', verbose_name='Patient')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Updated By')),
            ],
            options={
                'verbose_name': 'InnerHealth Abstract Class',
            },
        ),
    ]