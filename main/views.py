from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("QUACK!
                        <p><b>/admin</b> - admin panel;</p>
                        <p><b>/courses/all</b> - all courses;</p>
                        <p><b>/courses/createcat</b> - create category;</p>
                        <p><b>/courses/createbr</b> - create branch;</p>
                        <p><b>/courses/createcon</b> - create contact;</p>
                        <p><b>/courses/createcou</b> - create course.</p>")
