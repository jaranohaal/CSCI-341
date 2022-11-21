from django.urls import path
from . import views


urlpatterns = [
    #BASIC URLS:
    path('', views.home,name="home"),
    path('users/', views.users, name="users"),
    path('country/', views.country,name="country"),
    path('disease_type/', views.disease_type,name='disease_type'),
    path('disease/', views.disease,name='disease'),
    path('discover/', views.discover,name='discover'),
    path('doctor/', views.doctor,name='doctor'),
    path('public_servant/', views.public_servant,name='public_servant'),
    path('records/', views.records,name='records'),
    path('specialize/', views.specialize,name='specialize'),
    #CRUD URLS:

    #Country
    path('create_country/',views.create_country,name='create_country'),
    path('update_country/<str:pk>',views.update_country,name='update_country'),
    path('delete_country/<str:pk>',views.delete_country,name='delete_country'),

    #DiseaseType
    path('create_diseasetype/',views.create_diseasetype,name='create_diseasetype'),
    path('update_diseasetype/<str:pk>',views.update_diseasetype,name='update_diseasetype'),
    path('delete_diseasetype/<str:pk>',views.delete_diseasetype,name='delete_diseasetype'),

    #Disease
    path('create_disease/',views.create_disease,name='create_disease'),
    path('update_disease/<str:pk>',views.update_disease,name='update_disease'),
    path('delete_disease/<str:pk>',views.delete_disease,name='delete_disease'),
    
    #Discover
    path('create_discover/',views.create_discover,name='create_discover'),
    path('update_discover/<str:pk>',views.update_discover,name='update_discover'),
    path('delete_discover/<str:pk>',views.delete_discover,name='delete_discover'),

    #Doctor
    path('create_doctor/',views.create_doctor,name='create_doctor'),
    path('update_doctor/<str:pk>',views.update_doctor,name='update_doctor'),
    path('delete_doctor/<str:pk>',views.delete_doctor,name='delete_doctor'),

    #Users
    path('create_user/',views.create_user,name='create_user'),
    path('update_user/<str:pk>',views.update_user,name='update_user'),
    path('delete_user/<str:pk>',views.delete_user,name='delete_user'),

    #Public servant
    path('create_ps/',views.create_ps,name='create_ps'),
    path('update_ps/<str:pk>',views.update_ps,name='update_ps'),
    path('delete_ps/<str:pk>',views.delete_ps,name='delete_ps'),

    #Specialize
    path('create_spec/',views.create_spec,name='create_spec'),
    path('update_spec/<str:pk>',views.update_spec,name='update_spec'),
    path('delete_spec/<str:pk>',views.delete_spec,name='delete_spec'),

    #Records
    path('create_rec/',views.create_rec,name='create_rec'),
    path('update_rec/<str:pk>',views.update_rec,name='update_rec'),
    path('delete_rec/<str:pk>',views.delete_rec,name='delete_rec'),
    
]
