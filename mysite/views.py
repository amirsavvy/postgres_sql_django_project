from django.shortcuts import render
from django.http import Http404, HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html', {})

