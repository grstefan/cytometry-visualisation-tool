from django.db import models


class Boxplot(models.Model):
    index = models.IntegerField(primary_key=True, blank=False, null=False)
    attribute = models.TextField(blank=True, null=True)
    avg = models.FloatField(blank=True, null=True)
    class_field = models.TextField(db_column='class', blank=True,
                                   null=True)  # Field renamed because it was a Python reserved word.
    max = models.FloatField(blank=True, null=True)
    min = models.FloatField(blank=True, null=True)
    q1 = models.FloatField(blank=True, null=True)
    q3 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'boxplot'


class Clusters(models.Model):
    index = models.IntegerField(primary_key=True, blank=False, null=False)
    cd34 = models.FloatField(db_column='CD34', blank=True, null=True)  # Field name made lowercase.
    cd10 = models.FloatField(db_column='CD10', blank=True, null=True)  # Field name made lowercase.
    cd19 = models.FloatField(db_column='CD19', blank=True, null=True)  # Field name made lowercase.
    cd27 = models.FloatField(db_column='CD27', blank=True, null=True)  # Field name made lowercase.
    igm = models.FloatField(db_column='IgM', blank=True, null=True)  # Field name made lowercase.
    igd = models.FloatField(db_column='IgD', blank=True, null=True)  # Field name made lowercase.
    cd138 = models.FloatField(db_column='CD138', blank=True, null=True)  # Field name made lowercase.
    cd20 = models.FloatField(db_column='CD20', blank=True, null=True)  # Field name made lowercase.
    cd22 = models.FloatField(db_column='CD22', blank=True, null=True)  # Field name made lowercase.
    igg = models.FloatField(db_column='IgG', blank=True, null=True)  # Field name made lowercase.
    iga = models.FloatField(db_column='IgA', blank=True, null=True)  # Field name made lowercase.
    cd38 = models.FloatField(db_column='CD38', blank=True, null=True)  # Field name made lowercase.
    cd45 = models.FloatField(db_column='CD45', blank=True, null=True)  # Field name made lowercase.
    tmp_class = models.TextField(blank=True, null=True)
    tmp_color = models.TextField(blank=True, null=True)
    have_class = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clusters'


class HeatMap(models.Model):
    index = models.IntegerField(primary_key=True, blank=False, null=False)
    bckg190di = models.FloatField(db_column='BCKG190Di', blank=True, null=True)  # Field name made lowercase.
    ba138di = models.FloatField(db_column='Ba138Di', blank=True, null=True)  # Field name made lowercase.
    beads_ce140 = models.FloatField(db_column='Beads-Ce140', blank=True,
                                    null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cd10 = models.FloatField(db_column='CD10', blank=True, null=True)  # Field name made lowercase.
    cd138 = models.FloatField(db_column='CD138', blank=True, null=True)  # Field name made lowercase.
    cd184 = models.FloatField(db_column='CD184', blank=True, null=True)  # Field name made lowercase.
    cd19 = models.FloatField(db_column='CD19', blank=True, null=True)  # Field name made lowercase.
    cd20 = models.FloatField(db_column='CD20', blank=True, null=True)  # Field name made lowercase.
    cd200 = models.FloatField(db_column='CD200', blank=True, null=True)  # Field name made lowercase.
    cd22 = models.FloatField(db_column='CD22', blank=True, null=True)  # Field name made lowercase.
    cd24 = models.FloatField(db_column='CD24', blank=True, null=True)  # Field name made lowercase.
    cd243 = models.FloatField(db_column='CD243', blank=True, null=True)  # Field name made lowercase.
    cd269 = models.FloatField(db_column='CD269', blank=True, null=True)  # Field name made lowercase.
    cd27 = models.FloatField(db_column='CD27', blank=True, null=True)  # Field name made lowercase.
    cd289 = models.FloatField(db_column='CD289', blank=True, null=True)  # Field name made lowercase.
    cd3_cd14_cd15 = models.FloatField(db_column='CD3&CD14&CD15', blank=True,
                                      null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cd319 = models.FloatField(db_column='CD319', blank=True, null=True)  # Field name made lowercase.
    cd325 = models.FloatField(db_column='CD325', blank=True, null=True)  # Field name made lowercase.
    cd329 = models.FloatField(db_column='CD329', blank=True, null=True)  # Field name made lowercase.
    cd338 = models.FloatField(db_column='CD338', blank=True, null=True)  # Field name made lowercase.
    cd34 = models.FloatField(db_column='CD34', blank=True, null=True)  # Field name made lowercase.
    cd362 = models.FloatField(db_column='CD362', blank=True, null=True)  # Field name made lowercase.
    cd38 = models.FloatField(db_column='CD38', blank=True, null=True)  # Field name made lowercase.
    cd44 = models.FloatField(db_column='CD44', blank=True, null=True)  # Field name made lowercase.
    cd45 = models.FloatField(db_column='CD45', blank=True, null=True)  # Field name made lowercase.
    cd47 = models.FloatField(db_column='CD47', blank=True, null=True)  # Field name made lowercase.
    cs133di = models.FloatField(db_column='Cs133Di', blank=True, null=True)  # Field name made lowercase.
    dna1 = models.FloatField(db_column='DNA1', blank=True, null=True)  # Field name made lowercase.
    dna2 = models.FloatField(db_column='DNA2', blank=True, null=True)  # Field name made lowercase.
    event_length = models.FloatField(db_column='Event_length', blank=True, null=True)  # Field name made lowercase.
    iga = models.FloatField(db_column='IgA', blank=True, null=True)  # Field name made lowercase.
    igd = models.FloatField(db_column='IgD', blank=True, null=True)  # Field name made lowercase.
    igg = models.FloatField(db_column='IgG', blank=True, null=True)  # Field name made lowercase.
    igm = models.FloatField(db_column='IgM', blank=True, null=True)  # Field name made lowercase.
    klf_4 = models.FloatField(db_column='KLF-4', blank=True,
                              null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nanog = models.FloatField(db_column='Nanog', blank=True, null=True)  # Field name made lowercase.
    nestin = models.FloatField(db_column='Nestin', blank=True, null=True)  # Field name made lowercase.
    notch_1 = models.FloatField(db_column='Notch-1', blank=True,
                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    oct3_4 = models.FloatField(db_column='Oct3/4', blank=True,
                               null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pca_1 = models.FloatField(db_column='PCA_1', blank=True, null=True)  # Field name made lowercase.
    pca_2 = models.FloatField(db_column='PCA_2', blank=True, null=True)  # Field name made lowercase.
    pca_3 = models.FloatField(db_column='PCA_3', blank=True, null=True)  # Field name made lowercase.
    rara2 = models.FloatField(db_column='RARa2', blank=True, null=True)  # Field name made lowercase.
    sox_2 = models.FloatField(db_column='Sox-2', blank=True,
                              null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    viability = models.FloatField(db_column='Viability', blank=True, null=True)  # Field name made lowercase.
    xe131di = models.FloatField(db_column='Xe131Di', blank=True, null=True)  # Field name made lowercase.
    cl_parp = models.FloatField(db_column='cl. PARP', blank=True,
                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cl_caspase_3 = models.FloatField(db_column='cl. caspase-3', blank=True,
                                     null=True)  # Field renamed to remove unsuitable characters.
    cyto_kappa = models.FloatField(db_column='cyto kappa', blank=True,
                                   null=True)  # Field renamed to remove unsuitable characters.
    cyto_lambda = models.FloatField(db_column='cyto lambda', blank=True,
                                    null=True)  # Field renamed to remove unsuitable characters.
    file_name = models.TextField(blank=True, null=True)
    tsne_1 = models.FloatField(db_column='tSNE_1', blank=True, null=True)  # Field name made lowercase.
    tsne_2 = models.FloatField(db_column='tSNE_2', blank=True, null=True)  # Field name made lowercase.
    tsne_3 = models.FloatField(db_column='tSNE_3', blank=True, null=True)  # Field name made lowercase.
    tmp_class = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'heat_map'


class LoadedData(models.Model):
    index = models.IntegerField(primary_key=True, blank=False, null=False)
    time = models.FloatField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    event_length = models.IntegerField(db_column='Event_length', blank=True, null=True)  # Field name made lowercase.
    viability = models.FloatField(db_column='Viability', blank=True, null=True)  # Field name made lowercase.
    cl_parp = models.FloatField(db_column='cl. PARP', blank=True,
                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cl_caspase_3 = models.FloatField(db_column='cl. caspase-3', blank=True,
                                     null=True)  # Field renamed to remove unsuitable characters.
    xe131di = models.FloatField(db_column='Xe131Di', blank=True, null=True)  # Field name made lowercase.
    cs133di = models.FloatField(db_column='Cs133Di', blank=True, null=True)  # Field name made lowercase.
    ba138di = models.FloatField(db_column='Ba138Di', blank=True, null=True)  # Field name made lowercase.
    cd44 = models.FloatField(db_column='CD44', blank=True, null=True)  # Field name made lowercase.
    beads_ce140 = models.FloatField(db_column='Beads-Ce140', blank=True,
                                    null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cd200 = models.FloatField(db_column='CD200', blank=True, null=True)  # Field name made lowercase.
    cd19 = models.FloatField(db_column='CD19', blank=True, null=True)  # Field name made lowercase.
    cd3_cd14_cd15 = models.FloatField(db_column='CD3&CD14&CD15', blank=True,
                                      null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cd47 = models.FloatField(db_column='CD47', blank=True, null=True)  # Field name made lowercase.
    cd243 = models.FloatField(db_column='CD243', blank=True, null=True)  # Field name made lowercase.
    cd24 = models.FloatField(db_column='CD24', blank=True, null=True)  # Field name made lowercase.
    cd20 = models.FloatField(db_column='CD20', blank=True, null=True)  # Field name made lowercase.
    iga = models.FloatField(db_column='IgA', blank=True, null=True)  # Field name made lowercase.
    cd184 = models.FloatField(db_column='CD184', blank=True, null=True)  # Field name made lowercase.
    igd = models.FloatField(db_column='IgD', blank=True, null=True)  # Field name made lowercase.
    rara2 = models.FloatField(db_column='RARa2', blank=True, null=True)  # Field name made lowercase.
    cd38 = models.FloatField(db_column='CD38', blank=True, null=True)  # Field name made lowercase.
    igg = models.FloatField(db_column='IgG', blank=True, null=True)  # Field name made lowercase.
    cd45 = models.FloatField(db_column='CD45', blank=True, null=True)  # Field name made lowercase.
    cd362 = models.FloatField(db_column='CD362', blank=True, null=True)  # Field name made lowercase.
    cd10 = models.FloatField(db_column='CD10', blank=True, null=True)  # Field name made lowercase.
    cd325 = models.FloatField(db_column='CD325', blank=True, null=True)  # Field name made lowercase.
    cd22 = models.FloatField(db_column='CD22', blank=True, null=True)  # Field name made lowercase.
    notch_1 = models.FloatField(db_column='Notch-1', blank=True,
                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cd329 = models.FloatField(db_column='CD329', blank=True, null=True)  # Field name made lowercase.
    cd34 = models.FloatField(db_column='CD34', blank=True, null=True)  # Field name made lowercase.
    cd269 = models.FloatField(db_column='CD269', blank=True, null=True)  # Field name made lowercase.
    nanog = models.FloatField(db_column='Nanog', blank=True, null=True)  # Field name made lowercase.
    cyto_kappa = models.FloatField(db_column='cyto kappa', blank=True,
                                   null=True)  # Field renamed to remove unsuitable characters.
    sox_2 = models.FloatField(db_column='Sox-2', blank=True,
                              null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cd27 = models.FloatField(db_column='CD27', blank=True, null=True)  # Field name made lowercase.
    oct3_4 = models.FloatField(db_column='Oct3/4', blank=True,
                               null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    klf_4 = models.FloatField(db_column='KLF-4', blank=True,
                              null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    igm = models.FloatField(db_column='IgM', blank=True, null=True)  # Field name made lowercase.
    nestin = models.FloatField(db_column='Nestin', blank=True, null=True)  # Field name made lowercase.
    cd138 = models.FloatField(db_column='CD138', blank=True, null=True)  # Field name made lowercase.
    cd289 = models.FloatField(db_column='CD289', blank=True, null=True)  # Field name made lowercase.
    cyto_lambda = models.FloatField(db_column='cyto lambda', blank=True,
                                    null=True)  # Field renamed to remove unsuitable characters.
    cd338 = models.FloatField(db_column='CD338', blank=True, null=True)  # Field name made lowercase.
    cd319 = models.FloatField(db_column='CD319', blank=True, null=True)  # Field name made lowercase.
    bckg190di = models.FloatField(db_column='BCKG190Di', blank=True, null=True)  # Field name made lowercase.
    dna1 = models.FloatField(db_column='DNA1', blank=True, null=True)  # Field name made lowercase.
    dna2 = models.FloatField(db_column='DNA2', blank=True, null=True)  # Field name made lowercase.
    pca_1 = models.FloatField(db_column='PCA_1', blank=True, null=True)  # Field name made lowercase.
    pca_2 = models.FloatField(db_column='PCA_2', blank=True, null=True)  # Field name made lowercase.
    pca_3 = models.FloatField(db_column='PCA_3', blank=True, null=True)  # Field name made lowercase.
    tsne_1 = models.FloatField(db_column='tSNE_1', blank=True, null=True)  # Field name made lowercase.
    tsne_2 = models.FloatField(db_column='tSNE_2', blank=True, null=True)  # Field name made lowercase.
    tsne_3 = models.FloatField(db_column='tSNE_3', blank=True, null=True)  # Field name made lowercase.
    tmp_class = models.TextField(blank=True, null=True)
    file_name = models.TextField(blank=True, null=True)
    k_mean = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loaded_data'
