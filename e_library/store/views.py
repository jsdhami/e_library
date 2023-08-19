from django.shortcuts import render, HttpResponse

def index(request):

 # return HttpResponse("Hello, world. You're at the polls index.")
#  this is for adding variable in front page like as date authors etc
 context = {
    'variable':'message',
    'postfirst':'About Janak',
    'postsecond':'About projects',
 }
 return render(request, 'index.html', context)
   
def about(request):
    # return HttpResponse("hello guys")
    return render(request, 'about.html')

def services(request):
    # return HttpResponse("hello guys this arr are services")
     return render(request, 'services.html')

def contact(request):
    # return HttpResponse("hello guys this all about contact form")
     return render(request, 'contact.html')