from django.core.urlresolvers import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,RequestContext
from django.contrib.auth.decorators import login_required
from lyblog.common.CommonPaginator import SelfPaginator
from blog.views.permission import PermissionVerify
from blog.views.role import AddRole

from django.contrib import auth
from django.contrib.auth import get_user_model
from blog.forms import LoginUserForm,ChangePasswordForm,AddUserForm,EditUserForm
def LoginUser(request):
    '''用户登录view'''
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    if request.method == 'GET' and request.GET.has_key('next'):
        next = request.GET['next']
    else:
        next = '/'

    if request.methos == 'POST':
        form = LoginUserForm(request,data=request.POST)
        if form.is_valid():
            auth.login(request,form.get_user())
            return HttpResponseRedirect(request.POST['next'])
    else:
        form = LoginUserForm(request)

    kwvars = {
        'request':request,
        'form':form,
        'next':next,
    }
    return render_to_response('blog/login.html',kwvars,RequestContext(request))

@login_required
def LogoutUser(request):
    auth.logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

@login_required
def ChangePassword(request):
    if request.method == 'POST':
        form = ChangePasswordForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('logouturl'))
    else:
        form = ChangePasswordForm(user=request.user)
    kwvars = {
        'form':form,
        'request':request,
    }
    return render_to_response('blog/password.change.html',kwvars,RequestContext(request))

@login_required
@PermissionVerify()
def ListUser(request):
    mList = get_user_model().objects.all()
    lst = SelfPaginator(request,mList,20)
    kwvars = {
        'lPage':lst,
        'request':request,
    }
    return render_to_response('blog/user.list.html',kwvars,RequestContext(request))

@login_required
@PermissionVerify()
def AddUser(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])

            form.save()
            return HttpResponseRedirect(reverse('listuserurl'))
    else:
        form = AddUserForm()
    kwvars = {
        'form':form,
        'request':request,
    }
    return render_to_response('blog/user.add.html',kwvars,RequestContext(request))

@login_required
@PermissionVerify()
def EditUser(request,ID):
    user = get_user_model().objects.get(id=ID)
    if request.method == 'POST':



