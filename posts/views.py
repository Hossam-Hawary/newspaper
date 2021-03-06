from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.paginator import Paginator
from django.shortcuts import render
from models import Post,Section,tags
# Create your views here.



def index_pag(request):
	queryset_list = Post.objects.all().order_by('-date') #3shan t get desending
	paginator = Paginator(queryset_list,3)
	page_num=request.GET.get('page')
	try:
        	queryset = paginator.page(page_num)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        	queryset = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        	queryset = paginator.page(paginator.num_pages)
	user=request.user
	if user.is_anonymous():
		user=None
	return render(request, 'home1.html',{"queryset":queryset,'user':user})


def index_pag1(request,section_num):
	section = Section.objects.filter(id=section_num)
	queryset_list = Post.objects.filter(section_name_id= section_num).order_by('-date')
	#queryset_list = Post.objects.all().order_by('-date') #3shan t get desending
	paginator = Paginator(queryset_list,5)
	page_num=request.GET.get('page')
	try:
        	queryset = paginator.page(page_num)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        	queryset = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        	queryset = paginator.page(paginator.num_pages)
	user=request.user
	if user.is_anonymous():
		user=None
	return render(request, 'detail.html',{"queryset":queryset , "section" :section,'user':user})

def postt(request,question_num):
	posts = Post.objects.filter(id= question_num)
	tags2=tags.objects.filter(post_id=question_num)
	user=request.user
	if user.is_anonymous():
		user=None
	context = {'posts': posts,'tags2':tags2,'user':user}

	return render(request,'post.html',context)



def tag(request,tag_id):
	tag_obj=tags.objects.get(id=tag_id)
	posts_id = tags.objects.values_list('post_id',flat=True).filter(tag_name=tag_obj.tag_name)
	queryset_list = []
	for i in posts_id:
		post = Post.objects.get(id=i)
		queryset_list.append(post)
	paginator = Paginator(queryset_list,5)
	page_num=request.GET.get('page')
	try:
        	queryset = paginator.page(page_num)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        	queryset = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        	queryset = paginator.page(paginator.num_pages)
	user=request.user
	if user.is_anonymous():
		user=None
	return render(request, 'tag.html',{"queryset":queryset ,'user':user})







