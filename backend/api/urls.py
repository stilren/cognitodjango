from django.urls import path
from . import views

urlpatterns = [
    path('api/chore/', views.ChoreListCreate.as_view() ),
]