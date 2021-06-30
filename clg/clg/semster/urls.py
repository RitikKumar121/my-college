from django.urls import path
from semster import views
urlpatterns = [
    path('semster1/', views.semster1),
    path('semster2/', views.semster2),
    path('semster3/', views.semster3),
    path('semster4/', views.semster4),
    path('semster5/', views.semster5),
    path('semster6/', views.semster6),
    path('semster7/', views.semster7),
    path('semster8/', views.semster8),
    path('sem1sub/',views.sem1sub),
    path('sem2sub/',views.sem2sub),
    path('sem3sub/',views.sem3sub),
    path('sem4sub/',views.sem4sub),


]
