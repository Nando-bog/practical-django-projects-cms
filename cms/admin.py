# coding=utf-8
# Code for the FlatPage CKEditortaken from https://gist.github.com/elidickinson/1379652

from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from search.models import SearchKeyword
 
# Note: we are renaming the original Admin and Form as we import them!
from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld
from django.contrib.flatpages.admin import FlatpageForm as FlatpageFormOld
 
from django import forms
from ckeditor.widgets import CKEditorWidget
 
class FlatpageForm(FlatpageFormOld):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = FlatPage # this is not automatically inherited from FlatpageFormOld
 
 
class KeywordInline(admin.TabularInline):
    model = SearchKeyword
 
class FlatPageAdmin(FlatPageAdminOld):
    form = FlatpageForm
    inlines= [
        KeywordInline,
    ]
 
 
# We have to unregister the normal admin, and then reregister ours
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
admin.site.register(SearchKeyword)

##Inlines for the keyword App
