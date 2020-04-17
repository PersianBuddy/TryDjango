from django.urls import path
from .views import courses_list_view

app_name = 'courses'
urlpatterns = [
    path('', courses_list_view, name = 'courses_list')
]