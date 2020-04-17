from django.urls import path
from .views import CourseListView, CourseDetailView, CourseCreateView, CourseUpdateView, CourseDeleteView

app_name = 'courses'
urlpatterns = [
    path('', CourseListView.as_view(), name = 'courses_list'),
    path('course/<int:id>/', CourseDetailView.as_view(), name = 'course_detail'),
    path('create/', CourseCreateView.as_view(), name = 'create_course'),
    path('course/<int:id>/update/', CourseUpdateView.as_view(), name = 'course_update'),
    path('course/<int:id>/delete/', CourseDeleteView.as_view(), name = 'course_delete'),
]