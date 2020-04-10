from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request,*args, **kwargs):
    item_dictionary = {
        "school" : "Oxford",
        "major" : "my Major",
        "student_list" : ["Shahin", "Sara", "Joe"]
    }
    my_name = "Shahn Najafi"
    return render(request, "home.html", item_dictionary)