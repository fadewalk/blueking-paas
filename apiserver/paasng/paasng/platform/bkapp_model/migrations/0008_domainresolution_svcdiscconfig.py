# Generated by Django 3.2.12 on 2023-11-03 07:27

from django.db import migrations, models
import django.db.models.deletion
import paasng.platform.bkapp_model.models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0009_application_is_scene_app'),
        ('bkapp_model', '0007_auto_20231024_1450'),
    ]

    operations = [
        migrations.CreateModel(
            name='SvcDiscConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('bk_saas', paasng.platform.bkapp_model.models.BkSaaSField(default=list)),
                ('application', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='applications.application', unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DomainResolution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('nameservers', paasng.platform.bkapp_model.models.NameServersField(default=list, help_text='k8s dnsConfig nameServers')),
                ('host_aliases', paasng.platform.bkapp_model.models.HostAliasesField(default=list, help_text='k8s hostAliases')),
                ('application', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='applications.application', unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
