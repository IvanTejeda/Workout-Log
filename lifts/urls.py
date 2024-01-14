from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.main, name="main"),
    path('log/', views.log, name = "log"),
    
    
    path('bench/<int:id>/change/', views.bench_update, name = 'bench-update'),
    path('squat/<int:id>/change/', views.squat_update, name = 'squat-update'),
    path('dead/<int:id>/change/', views.dead_update, name = 'dead-update'),


    path('bench/<int:id>/delete', views.bench_delete, name="bench-delete"),
    path('squat/<int:id>/delete', views.squat_delete, name="squat-delete"),
    path('dead/<int:id>/delete', views.dead_delete, name="dead-delete"),


    path('bench/add/', views.bench_create, name = 'bench-create'),
    path('squat/add/', views.squat_create, name = 'squat-create'),
    path('dead/add/', views.dead_create, name = 'dead-create'),

    path('bench/details/', views.bench_details, name = 'bench-details'),
    path('squat/details/', views.squat_details, name = 'squat-details'),
    path('dead/details/', views.dead_details, name = 'dead-details'),
    

    path('bench/graph', views.bench_graph, name = 'bench-graph'),
    path('squat/graph', views.squat_graph, name = 'squat-graph'),
    path('dead/graph', views.dead_graph, name = 'dead-graph'),
]
