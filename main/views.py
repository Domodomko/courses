from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("QUACK! /admin; /courses/all - all courses; /courses/createcat - create category; /courses/createbr - create branch; /courses/createcon - create contact; /courses/createcou - create course")
