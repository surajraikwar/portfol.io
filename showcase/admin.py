from django.contrib import admin
from .models import Account, Project


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'is_admin']
    search_fields = ['email', 'first_name', 'last_name']
    list_filter = ['is_admin', 'portfolio_template']
    ordering = ['-id']
    

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'account', 'is_featured', 'created_at']
    search_fields = ['project_name', 'description', 'tech_stack']
    list_filter = ['is_featured', 'created_at']
    date_hierarchy = 'created_at'
    ordering = ['-created_at']


# Customize admin site header
admin.site.site_header = "DevShowcase Admin"
admin.site.site_title = "DevShowcase Admin Portal"
admin.site.index_title = "Welcome to DevShowcase Administration"
