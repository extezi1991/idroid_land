from django.contrib import admin
from .models import *


class SubscriberAdmin (admin.ModelAdmin):
    # list_display = ["name", "email"]
    list_display = [field.name for field in Message._meta.fields]
    list_filter = ['name']
    search_fields = ['name', 'email','text']

    fields = ["email", 'name', 'text']

    # exclude = ["email"]
	# inlines = [FieldMappingInline]
	# fields = []
    # #exclude = ["type"]
	# #list_filter = ('report_data',)
	# search_fields = ['category', 'subCategory', 'suggestKeyword']

    class Meta:
        model = Message
admin.site.register(Message, SubscriberAdmin)