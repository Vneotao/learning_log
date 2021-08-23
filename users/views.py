from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http.response import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def logout_view(request):
    """用户注销"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))


def register(request):
    """用户注册"""
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # 让用户自动登录, 再重定向到主页
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))
    context = {'form': form}
    return render(request, 'users/register.html', context)