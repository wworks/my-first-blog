from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from django.shortcuts import redirect
from .push import Push
from .forms import PostForm

# Create your views here.
def home(request):
    return render(request, 'blog/home.html')
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
def push(request):
    posts = Post.objects.all()
    response = Push.Push('derp',posts)
        
    return render(request, 'blog/push.html', {'response': response})
def xml(request):
    posts = Post.objects.all()
       
    return render(request, 'blog/xml.html', {'posts': posts})
def register(request,naam,klas,regid):
    #if request.method == "POST":
        # klas = request.POST.__getitem__('klas')
        #regid = request.POST.__getitem__('regid')
        #naam = request.POST.__getitem__('naam')
    if naam != "" and klas != "" and regid != "":
        Post.objects.create(naam = naam,klas = klas, regid = regid)
    return render(request,"blog/empty.html")