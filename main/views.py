from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("QUACK!<p>/admin - admin panel;
                        <p><b>/courses/all</b> - all courses;
                        <p><b>/courses/createcat</b> - create category;
                        <p><b>/courses/createbr</b> - create branch;
                        <p><b>/courses/createcon</b> - create contact;
                        <p><b>/courses/createcou</b> - create course.")
