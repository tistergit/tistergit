'''
Created on 2011-8-13

@author: tister
'''
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required


@login_required
def hello(request):
    return render_to_response('hello.html')