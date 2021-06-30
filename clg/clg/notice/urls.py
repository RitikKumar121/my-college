from django.urls import path
from notice import views
urlpatterns = [
    path('notice/', views.notice),



]
