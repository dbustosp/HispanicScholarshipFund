from django.contrib import admin
from textapp.models import *

class NewAdmin(admin.ModelAdmin):
    pass

class NewsletterAdmin(admin.ModelAdmin):
	pass

class CategoryRegistrationAdmin(admin.ModelAdmin):
	pass

class CategoryKeydateAdmin(admin.ModelAdmin):
	pass

class KeydateAdmin(admin.ModelAdmin):
	pass

admin.site.register(New, NewAdmin)
admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(CategoryRegistration, CategoryRegistrationAdmin)
admin.site.register(Keydatecategory, CategoryKeydateAdmin)
admin.site.register(Keydate, KeydateAdmin)