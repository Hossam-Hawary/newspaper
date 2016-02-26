from django.shortcuts import render
from models import Post
# Create your views here.
def index(request):

	post = Post.objects.get(id=2)
	context = {'post':post}
	return render(request,'index.html',context)

def home(request):

	posts = Post.objects.all().order_by('-date') #3shan t get desending
	context = {'posts':posts}
	return render(request,'home.html',context)

