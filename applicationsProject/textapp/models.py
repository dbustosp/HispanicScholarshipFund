from django.db import models
from django.contrib.auth.models import User


class CategoryRegistration(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return unicode(self.name)

class Newsletter(models.Model):
	kind = models.CharField(max_length=100, blank=False)

	def __unicode__(self):
		return unicode(self.kind)

class New(models.Model):
	title = models.CharField(max_length=100, blank=False)
	content = models.TextField(blank=False)
	kind = models.ForeignKey(Newsletter)

	def __unicode__(self):
		return unicode(self.title)

class Request(models.Model):
	kind = models.CharField(max_length=100)
	number = models.BigIntegerField(blank = False)
	name = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)
	email = models.EmailField()

	def __unicode__(self):
		return unicode(self.name)

class Keydate(models.Model):
	date = models.DateField()

	def __unicode__(self):
		return unicode(self.date)

class RegistrationCategory(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return unicode(self.name)


class Applicant(models.Model):
	user = models.OneToOneField(User)
	news = models.ManyToManyField(New)
	requests = models.ManyToManyField(Request)
	keydates = models.ManyToManyField(Keydate)
	kinds = models.ManyToManyField(CategoryRegistration)

	def __unicode__(self):
		return unicode(self.user)


class Apply(models.Model):
	user = models.ForeignKey(Applicant)

	def __unicode__(self):
		return unicode(self.user)

class Donation(models.Model):
	number = models.BigIntegerField(blank = False)
	amount = models.BigIntegerField(blank = False)
	user = models.ForeignKey(Applicant)

	def __unicode__(self):
		return unicode(self.number)


class Keydatecategory(models.Model):
	kind = models.CharField(max_length=100)

	def __unicode__(self):
		return unicode(self.kind)















