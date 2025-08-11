from django.urls import path
from . import views

app_name = 'userideabajet'

urlpatterns = [
    path('', views.user_home, name='user_home'),
    path('submit/', views.submit_budget_idea, name='submit_budget_idea'),
    path('status/<int:submission_id>/', views.submission_status, name='submission_status'),
]
