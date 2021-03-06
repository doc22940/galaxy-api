# Generated by Django 2.2.4 on 2019-09-05 13:09

from django.db import migrations
import galaxy_api.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('galaxy_api', '0003_remove_namespace_owners'),
        ('auth', '0011_update_proxy_permissions'),
        ('galaxy_auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.group',),
            managers=[
                ('objects', galaxy_api.auth.models.GroupManager()),
            ],
        ),
        migrations.DeleteModel(
            name='Tenant',
        ),
    ]
