from django.shortcuts import render
from models import Post

# Create your views here.

def index(request):
<<<<<<< HEAD
	post = Post.objects.get(id=1)
	context = {'post':post}
	return render(request,'show.html',context)
=======
    post = Post.objects.get(id=1)
    context = { 'post' :post}
    return render(request,'index.html',context)
>>>>>>> 4d484ae09a613278b4c566d2bd0b84077eaa2bc4
