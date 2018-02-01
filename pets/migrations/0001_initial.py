# Generated by Django 2.0.1 on 2018-02-01 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('owners', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Pet name')),
                ('breed', models.CharField(max_length=30, verbose_name='Breed')),
                ('age', models.IntegerField(default=0, verbose_name='Age')),
                ('sound', models.CharField(max_length=10, verbose_name='Sound')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='owners.Owner')),
            ],
        ),
    ]