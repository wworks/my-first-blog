from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from django.shortcuts import redirect



# Create your views here.
def home(request):
    return render(request, 'blog/home.html')
def xml(request):
    posts = Post.objects.all()
    return render(request, 'blog/xml.html', {'posts': posts})
def register(request,naam,klas,regid):
    if naam != "" and klas != "" and regid != "":
        Post.objects.create(naam = naam,klas = klas, regid = regid)
    return render(request,"blog/empty.html")