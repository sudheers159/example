from django.shortcuts import render
from myapp.models import sudhir


# Create your views here.
def blog(request):
    data=sudhir.objects.all()
    return render(request, 'blog.html',{'bl':data})
def about(request):
    return render(request, 'about_us.html')

def test(request):
    return render(request,'testpage.html')