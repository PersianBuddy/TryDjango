from django.shortcuts import render

# Create your views here.
def courses_list_view(request, *args, **kwargs):
    return render(request, 'courses/courses.html',{})