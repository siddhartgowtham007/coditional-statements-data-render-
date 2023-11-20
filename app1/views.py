from django.shortcuts import render

# Create your views here.

def forloop(request):
    d={'a':100,'b':300,'c':400,'d':200}
    return render(request,'drend.html',d)