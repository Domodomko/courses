from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("QUACK!<p>/admin - admin panel; /courses/all - all courses; <p>/courses/createcat - create category; <p>/courses/createbr - create branch; <p>/courses/createcon - create contact; <p>/courses/createcou - create course")
