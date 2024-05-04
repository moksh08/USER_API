# data_analysis_app/urls.py
from django.urls import path
from .views import data_tab, descriptive_statistics_tab, exploratory_data_analysis_tab, export_to_csv

urlpatterns = [
    path('data/', data_tab, name='data_tab'),
    path('descriptive-statistics/', descriptive_statistics_tab, name='descriptive_statistics_tab'),
    path('exploratory-data-analysis/', exploratory_data_analysis_tab, name='exploratory_data_analysis_tab'),
     path('export/csv/', export_to_csv, name='export_to_csv'),
]