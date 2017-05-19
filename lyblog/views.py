from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,RequestContext

@login_required
def Home(request):
    return render_to_response('home.html',locals(),RequestContext(request))