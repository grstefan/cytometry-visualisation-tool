from django.conf.urls import url
from webserver import views
from django.shortcuts import render

urlpatterns = [url(r'^heatmap/$', views.heatmap, name='heatmap'),
    url(r'^scatter-plot/$', views.scatter_plot, name='scatter_plot'),
    url(r'^tree&data=(?P<type_data>[a-zA-Z]+)$', views.tree, name='tree'),

    url(r'^getClasses/$', views.get_classes, name='get_classes'),
    url(r'^getAtributes/$', views.get_atributes, name='get_stributes'),
    url(r'^getAtributesClasses/$', views.get_classes_atributes, name='get_atributes_classes'),
    url(r'^getScatterData/', views.get_scatter_data, name='get_scatter_data'),

    url(r'^getHeatmapData/$', views.get_heatmap_data, name='heatmap'),
    url(r'^getBoxplotData/$', views.get_boxplot_data, name='boxplot'),
    # url(r'^boxplot/$', views.boxplot, name='boxplot'),
    url(r'^loadDataset/', views.loadData, name='load_data'),

    url(r'^sampleavarages/$', views.get_all_data, name='get_avarages'),
    url(r'^cleanDataset/', views.cleanData, name='clean_data'),
    url(r'^cleanClass/', views.cleanClass, name='clean_class'),

    url(r'^loadedDataset/$', views.loadedData, name='loaded_data'),
    url(r'^tmpClasses/', views.tmpClasses, name='tmp_classes'),

    url(r'^analyzeData/', views.analyzeData, name='analyze_data'),
    url(r'^postCluster', views.postCluster, name='post_cluster')

]
