from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<style>
                           li {
                            list-style-type: none;
                            line-height: 1.8;
                           }
                           ul {
                            margin-left: 0;
                            padding-left: 0;
                           }
                           a {
                            text-decoration: none;
                            color: white;
                           }
                           a:hover {
                            text-decoration: inherit;
                            color: white;
                           }
                        </style>
                        QUACK!
                        <ul>
                        <li><a href="/admin">/admin</a> - admin panel;</li>
                        <li><a href="/courses/all">/courses/all</a> - all courses;</li>
                        <li><a href="question.html">???</a></li>
                        <li><a style="color:black;" href="black.html">Sans</a></li>
                        <p><b>/courses/all</b> - all courses;</p>
                        <p><b>/courses/createcat</b> - create category;</p>
                        <p><b>/courses/createbr</b> - create branch;</p>
                        <p><b>/courses/createcon</b> - create contact;</p>
                        <p><b>/courses/createcou</b> - create course.</p>")
