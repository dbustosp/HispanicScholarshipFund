#encoding:utf-8
from django.contrib.auth.models import User, Group
from django.db import models
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response,get_object_or_404
from django.template import RequestContext
#from isportuapp.forms import *
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#from isportuapp.models import *

def home(request):
	return render_to_response('index.html',{}, context_instance = RequestContext(request))