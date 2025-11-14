from django.urls import path
from . import views

app_name='studio'
urlpatterns = [
    path('studio/', views.statistics, name="statistics"),
    path('studio/edit/<str:username>', views.edit_account, name="edit_account"),
]
