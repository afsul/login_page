
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from django.views.decorators.cache import cache_control
from django.contrib import messages

# Create your views here.
@cache_control(no_cache=True, must_revalidated=True, no_store=True)
def index(request):
    if request.session.has_key('user_login'):  
        return render(request, 'index.html')
    else:
        return redirect(login)
@cache_control(no_cache=True, must_revalidated=True, no_store=True)
def login(request):
    if request.session.has_key('user_login'):
         return render(request, 'index.html')
    else:
        if request.method =='POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            if username == 'afsul' and password == '1234':
                request.session['user_login'] = True
                return redirect(index)
            else:
                # messages.info(request,"invalid details",extra_tags="login_error")
                return render(request, 'login.html',{"login_error":"invalid credentials"})
        return render(request, 'login.html')
@cache_control(no_cache=True, must_revalidated=True, no_store=True)
def logout(request):
    del request.session['user_login']
    return redirect(login)
