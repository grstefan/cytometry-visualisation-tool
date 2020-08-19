# Generated by Django 2.1.7 on 2019-05-10 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webserver', '0002_pca_tsne'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeatMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(blank=True, null=True)),
                ('bckg190di', models.FloatField(blank=True, db_column='BCKG190Di', null=True)),
                ('ba138di', models.FloatField(blank=True, db_column='Ba138Di', null=True)),
                ('beads_ce140', models.FloatField(blank=True, db_column='Beads-Ce140', null=True)),
                ('cd10', models.FloatField(blank=True, db_column='CD10', null=True)),
                ('cd138', models.FloatField(blank=True, db_column='CD138', null=True)),
                ('cd184', models.FloatField(blank=True, db_column='CD184', null=True)),
                ('cd19', models.FloatField(blank=True, db_column='CD19', null=True)),
                ('cd20', models.FloatField(blank=True, db_column='CD20', null=True)),
                ('cd200', models.FloatField(blank=True, db_column='CD200', null=True)),
                ('cd22', models.FloatField(blank=True, db_column='CD22', null=True)),
                ('cd24', models.FloatField(blank=True, db_column='CD24', null=True)),
                ('cd243', models.FloatField(blank=True, db_column='CD243', null=True)),
                ('cd269', models.FloatField(blank=True, db_column='CD269', null=True)),
                ('cd27', models.FloatField(blank=True, db_column='CD27', null=True)),
                ('cd289', models.FloatField(blank=True, db_column='CD289', null=True)),
                ('cd3_cd14_cd15', models.FloatField(blank=True, db_column='CD3&CD14&CD15', null=True)),
                ('cd319', models.FloatField(blank=True, db_column='CD319', null=True)),
                ('cd325', models.FloatField(blank=True, db_column='CD325', null=True)),
                ('cd329', models.FloatField(blank=True, db_column='CD329', null=True)),
                ('cd338', models.FloatField(blank=True, db_column='CD338', null=True)),
                ('cd34', models.FloatField(blank=True, db_column='CD34', null=True)),
                ('cd362', models.FloatField(blank=True, db_column='CD362', null=True)),
                ('cd38', models.FloatField(blank=True, db_column='CD38', null=True)),
                ('cd44', models.FloatField(blank=True, db_column='CD44', null=True)),
                ('cd45', models.FloatField(blank=True, db_column='CD45', null=True)),
                ('cd47', models.FloatField(blank=True, db_column='CD47', null=True)),
                ('cs133di', models.FloatField(blank=True, db_column='Cs133Di', null=True)),
                ('dna1', models.FloatField(blank=True, db_column='DNA1', null=True)),
                ('dna2', models.FloatField(blank=True, db_column='DNA2', null=True)),
                ('event_length', models.FloatField(blank=True, db_column='Event_length', null=True)),
                ('iga', models.FloatField(blank=True, db_column='IgA', null=True)),
                ('igd', models.FloatField(blank=True, db_column='IgD', null=True)),
                ('igg', models.FloatField(blank=True, db_column='IgG', null=True)),
                ('igm', models.FloatField(blank=True, db_column='IgM', null=True)),
                ('klf_4', models.FloatField(blank=True, db_column='KLF-4', null=True)),
                ('nanog', models.FloatField(blank=True, db_column='Nanog', null=True)),
                ('nestin', models.FloatField(blank=True, db_column='Nestin', null=True)),
                ('notch_1', models.FloatField(blank=True, db_column='Notch-1', null=True)),
                ('oct3_4', models.FloatField(blank=True, db_column='Oct3/4', null=True)),
                ('rara2', models.FloatField(blank=True, db_column='RARa2', null=True)),
                ('sox_2', models.FloatField(blank=True, db_column='Sox-2', null=True)),
                ('viability', models.FloatField(blank=True, db_column='Viability', null=True)),
                ('xe131di', models.FloatField(blank=True, db_column='Xe131Di', null=True)),
                ('cl_parp', models.FloatField(blank=True, db_column='cl. PARP', null=True)),
                ('cl_caspase_3', models.FloatField(blank=True, db_column='cl. caspase-3', null=True)),
                ('cyto_kappa', models.FloatField(blank=True, db_column='cyto kappa', null=True)),
                ('cyto_lambda', models.FloatField(blank=True, db_column='cyto lambda', null=True)),
                ('file_name', models.TextField(blank=True, null=True)),
                ('tmp_class', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'heat_map',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='djangomigrations',
            options={},
        ),
    ]