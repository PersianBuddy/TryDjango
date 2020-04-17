from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Course
from .forms import CreateCourseForm

# Create your views here.
class CourseListView(View):
    template_name = 'courses/courses.html'
    # queryset = Course.objects.all()
    # def get_queryset(self):
    #     return self.queryset
    def get(self,request, *args, **kwargs):
        queryset = Course.objects.all()
        context = {'courses_list': queryset}
        return render(request, self.template_name, context)


class CourseDetailView(View):
    template_name = 'courses/course_detail.html'
    def get(self, request, id=None, *args, **kwargs):
        context = {}
        if id is not None:
            course_object = get_object_or_404(Course, id= id)
            context['course_object'] =  course_object
        return render(request, self.template_name, context)


class CourseCreateView(View):
    template_name = 'courses/create_course.html'
    def get(self, request, *args, **kwargs):
        form = CreateCourseForm()
        context= {'form':form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = CreateCourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(Course.get_absolute_url(self))
        context = {'form':form}
        return render(request, self.template_name, context)


class CourseUpdateView(View):
    template_name = 'courses/update_course.html'

    def get_object(self):
        id =self.kwargs.get('id')
        if id is not None:
            course_object =get_object_or_404(Course, id = id)
            return course_object

    def get(self, request, id =None, *args, **kwargs):
        if id is not  None:
            course_obj = self.get_object()
            form = CreateCourseForm(instance=course_obj)
            context= {'form':form}
            return render(request, self.template_name, context)

    def post(self, request, id =None, *args, **kwargs):
        if id is not None:
            course_obj = self.get_object()
            form = CreateCourseForm(request.POST, instance=course_obj)
            if form.is_valid():
                form.save()
                return redirect(Course.get_absolute_url(self)+f'course/{id}/')
            context = {'form':form}
            return render(request, self.template_name, context)


class CourseDeleteView(View):
    template_name = 'courses/delete_course.html'
    def get_object(self):
        id = self.kwargs.get('id')
        if id is not None:
            course_obj = get_object_or_404(Course, id = id)
            return course_obj

    def get(self, request , *args, **kwargs):
        context = {}
        course_obj = self.get_object()
        print(course_obj)
        if course_obj is not None:
            context['course_object'] =course_obj

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        course_obj = self.get_object()
        if course_obj is not None:
            course_obj.delete()
            return redirect(Course.get_absolute_url(self))
