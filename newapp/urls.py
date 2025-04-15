from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('studenti/', views.list_students,  name="list-students"),
    path('studenti/<pk>/', views.detail_student, name="detail-student"),
    path('ucitelia/', views.list_teachers,  name="list-students"),
    path('ucitelia/<pk>/', views.detail_ucitel, name="detail-ucitel"),
    path('triedy/', views.list_triedy,  name="list-students"),
    path('triedy/<pk>/', views.vypis_trieda, name="vypis-triedy"),
]