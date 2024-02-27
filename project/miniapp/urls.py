from django.urls import path

from . import views

urlpatterns = [
    path('randomnumber/', views.models_list),
    path('randomnumber_html/', views.post_list),
]