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
from twilio.rest import TwilioRestClient

from flask import Flask, request, redirect
import twilio.twiml



toNumber = 9139807603
task = "taskNewsletter_options"

	
def home(request):
	send(toNumber, request, task);
	return render_to_response('index.html',{}, context_instance = RequestContext(request))



def send(toNumber, request, task):
	account = "ACf86edf02d5bf5963bb33e620c98f7598" #hsf: AC814f6122defc4cf79f5c9360ed59cf02
	token   = "ab27305256e1afe2b9137c6d5e107319"   #hsf: 064c847fca4456b19cb84cc8b6658a96
	client  = TwilioRestClient(account, token)
	#obtain "to" parameter as variable-user number
	#change from to hsf number
	#change body


	if task == "taskDonate":
		messageBody = donate();
	elif task ==  "taskApply":
		messageBody = apply();
	elif task ==  "taskRegister":
		messageBody = register();
	elif task ==  "taskKeydates":
		messageBody = keydates();
	elif task ==  "taskNewsletter":
		messageBody = newsletter();
	elif task ==  "taskThankyou":
		messageBody = thankyou();
	elif task ==  "taskRegister_options":
		messageBody = register_option();
	elif task ==  "taskNewsletter_options":
		messageBody = newsletter_options();
	else:
		messageBody = "Invalid selection"
	print messageBody;
	message = client.sms.messages.create(to="+1"+str(toNumber), from_="+19139560227", body=messageBody)  
	return;
	#return render_to_response('index.html',{}, context_instance = RequestContext(request))
	#change index.html to different page

def donate ():
	return "URL link to Process DONATION: https://hsf.ejoinme.org/MyPages/DonationPage/tabid/27473/Default.aspx"

def thankyou ():
	return "Thank you, the Hispanic Scholarship Fund shall be in contact with you!"

def apply ():
	return "URL link to Apply to HSF https://apply.hsf.net/applications/"

def register ():
	return "Please send your information in the format: FIRST NAME, LAST NAME, and EMAIL"

def register_option():
	return "(text back one or more of the following numbers) \n R1- Scholarships \n R2- Donations \n R3- Newsletter \n R4- Resources \n R5- Internships \n R6- Volunteering \n R7- Mentoring \n R8- Being Mentored"

def keydates():
	return "(text back one or more of the following numbers) \n K1- HSF General Scholarships \n K2- HSF Specialty Scholarships \n K3- Gates Millenium Scholarships  (GMS) \n K4- High School eligible \n K5- College eligible \n K6- Graduate eligible \n K7- Post Graduate eligible"

def newsletter():
	return "Please send your information in the format: FIRST NAME, LAST NAME, and EMAIL"

#has some minor problems
def newsletter_options():
	return "(text back one or more of the following numbers) \n N1- Alumni \n N2- Scholars  N3- Amigo  N4- Community Partner  N5- Sponsor  N6- Dean’s List  N7- High Schoolers"

