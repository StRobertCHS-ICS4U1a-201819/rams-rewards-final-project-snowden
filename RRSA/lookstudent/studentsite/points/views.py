from django.http import HttpResponse


def index(request):
    return HttpResponse("class. You're at")
