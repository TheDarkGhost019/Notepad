from django.urls import path
from . import views

app_name='studio'
urlpatterns = [
    path('studio/<int:user>', views.statistics, name="statistics"),
    path('studio/<int:user>/edit', views.edit_account, name="edit_account"),
]
