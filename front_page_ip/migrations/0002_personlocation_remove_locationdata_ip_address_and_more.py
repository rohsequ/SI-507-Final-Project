# Generated by Django 4.1.2 on 2022-12-02 03:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('front_page_ip', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='p_city', to='front_page_ip.city')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='p_country', to='front_page_ip.country')),
                ('state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='p_state', to='front_page_ip.country')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='locationdata',
            name='ip_address',
        ),
        migrations.AlterField(
            model_name='locationdata',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='loc_city', to='front_page_ip.city'),
        ),
        migrations.AlterField(
            model_name='locationdata',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='loc_country', to='front_page_ip.country'),
        ),
        migrations.AlterField(
            model_name='locationdata',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='loc_state', to='front_page_ip.country'),
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
