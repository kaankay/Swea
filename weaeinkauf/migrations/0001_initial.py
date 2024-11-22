# Generated by Django 4.2.11 on 2024-05-09 23:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quelle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alt_id', models.IntegerField(default=0)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('quellendatum', models.DateField()),
                ('bemerkung', models.TextField(blank=True, null=True)),
                ('created_by', models.CharField(default='null', max_length=200)),
                ('quellenart', models.CharField(choices=[('Vertrag', 'Vertrag'), ('Schätzung', 'Schätzung'), ('Indikation', 'Indikation'), ('Angebot', 'Angebot')], default='Angebot', max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vertrag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('bemerkung', models.TextField(blank=True, null=True)),
                ('quellendatum', models.DateField(blank=True, null=True)),
                ('vertragsart', models.CharField(blank=True, max_length=200, null=True)),
                ('vertragsbeginn', models.DateField(blank=True, null=True)),
                ('lieferzeit', models.CharField(blank=True, max_length=200, null=True)),
                ('wetterrisiko', models.CharField(blank=True, max_length=200, null=True)),
                ('vertragskennung', models.CharField(blank=True, max_length=200, null=True)),
                ('sonderkuendigungsrecht', models.CharField(blank=True, max_length=500, null=True)),
                ('quellen_id', models.IntegerField(default=0)),
                ('created_by', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quelle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weaeinkauf.quelle')),
            ],
        ),
        migrations.CreateModel(
            name='Schaetzung',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('quellendatum', models.DateField(blank=True, null=True)),
                ('bemerkung', models.TextField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=200, null=True)),
                ('schaetzer', models.CharField(blank=True, max_length=200, null=True)),
                ('quellen_id', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quelle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weaeinkauf.quelle')),
            ],
        ),
        migrations.CreateModel(
            name='Indikation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('quellendatum', models.DateField(blank=True, null=True)),
                ('bemerkung', models.TextField(blank=True, null=True)),
                ('quellen_id', models.IntegerField(default=0)),
                ('created_by', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quelle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weaeinkauf.quelle')),
            ],
        ),
        migrations.CreateModel(
            name='Angebot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('quellendatum', models.DateField(blank=True, null=True)),
                ('bemerkung', models.TextField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=200, null=True)),
                ('wetterrisiko', models.CharField(blank=True, max_length=200, null=True)),
                ('angebotskennung', models.TextField(blank=True, null=True)),
                ('quellen_id', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quelle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weaeinkauf.quelle')),
            ],
        ),
    ]
