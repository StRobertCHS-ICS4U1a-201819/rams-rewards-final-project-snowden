from django.http import HttpResponse
#user submit score
def index(request, id):
    file = open("scorefile.txt", "w")
    #save id to text file
    file.write("retrieved score: "+id)

    file.close()
    #http reponse
    return HttpResponse("Your score is "+id)

