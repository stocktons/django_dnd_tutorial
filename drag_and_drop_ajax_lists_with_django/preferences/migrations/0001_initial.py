# Generated by Django 2.2.5 on 2021-09-22 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PartnerPreferences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='StudentUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='StudentPartnerPreferences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField()),
                ('order', models.IntegerField()),
                ('partnerpreferences', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='preferences.PartnerPreferences')),
                ('studentuser', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='preferences.StudentUser')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.AddField(
            model_name='partnerpreferences',
            name='partner',
            field=models.ManyToManyField(through='preferences.StudentPartnerPreferences', to='preferences.StudentUser'),
        ),
    ]
