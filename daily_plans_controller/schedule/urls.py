from . import views
import schedule.views as views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('practice/', views.practice, name='practice'),
]
