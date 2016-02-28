from django.shortcuts import render

# Create your views here.
from user_app.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from django.template import RequestContext


@csrf_protect
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            user.first_name=form.cleaned_data['first_name']
            user.last_name=form.cleaned_data['last_name']
            user.save()
            return HttpResponseRedirect('/user_app/register/success/')
    else:
        form = UserCreationForm()
    variables = RequestContext(request, {
    'form': form
    })
    request.session['age'] = 24
    request.session['fav_color'] = "purple"
    return render_to_response( 'register.html', variables,)
def register_success(request):
    return HttpResponse("Registration Successfully Done")

@login_required
def home(request):
    return render_to_response(
    'home1.html',
    { 'user': request.user,'age': request.session['age']})
