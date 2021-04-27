from django.shortcuts import render

# Create your views here.

def intro(request):

    data = {

   "Name" : "michaleb",

    "Track" : "Backend(Python)",

    "Message" : "Hi mentors!, thanks to all the members of your team. - P.S. -  I'm trying out 'templates' "

}
    return render(request, 'intro/index.html', {"data": data})



