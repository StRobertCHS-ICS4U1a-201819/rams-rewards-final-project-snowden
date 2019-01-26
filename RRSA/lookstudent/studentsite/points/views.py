from django.http import HttpResponse

def index(request, id):

# c = newkkkk()
#c.calculatein(id)

    return HttpResponse(request.method+"class.  You're at   "+id)
