from django.shortcuts import render

# Create your views here.
from user_app.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login,authenticate
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
            user=authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'])
            if user!=None:
                login(request,user)
            return HttpResponseRedirect('/home')
    else:
        form = UserCreationForm()
    variables = RequestContext(request, {
    'form': form
    })
    
    return render_to_response( 'register.html', variables,)

#logout_fun
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

