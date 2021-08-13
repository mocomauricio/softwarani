from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import *

# Register your models here.
@register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone', 'mobile']
    search_fields = ['first_name', 'last_name', 'email']
    ordering = ['first_name']
    list_per_page = 50

@register(Executive)
class ExecutiveAdmin(admin.ModelAdmin):
    list_display = ['partner', 'position']
    search_fields = ['partner__first_name', 'partner__last_name']
    ordering = ['position']
    list_per_page = 50

@register(JobOffer)
class JobOfferAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publication_date']
    search_fields = ['title']
    ordering = ['-id']
    list_per_page = 50

    def save_model(self, request, obj, form, change):
        if(not change):
            obj.author = request.user
        super().save_model(request, obj, form, change)

@register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at']
    search_fields = ['name', 'email', 'subject']
    ordering = ['-id']
    list_per_page = 50

@register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publication_date']
    search_fields = ['title']
    ordering = ['-id']
    list_per_page = 50

    def save_model(self, request, obj, form, change):
        if(not change):
            obj.author = request.user
        super().save_model(request, obj, form, change)


@register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ['title', 'file', 'upload_date']
    search_fields = ['title']
    ordering = ['-id']
    list_per_page = 50

@register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ['page', 'link']
    ordering = ['-id']
    list_per_page = 50