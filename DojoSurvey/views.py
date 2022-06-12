from django.shortcuts import render


from django.shortcuts import render
def index(request):

    return render(request, "index.html")
# Create your views here.

def result(request):

    context = {
        "name": request._post["name"],
      "location": request._post['location'],
        "language":request._post['language'],
        "commit": request._post['commit'],
    }

    return render(request, "result.html",context)
