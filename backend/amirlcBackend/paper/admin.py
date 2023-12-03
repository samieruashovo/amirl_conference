from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Paper

# Register your models here.


@admin.register(Paper)
class PaperAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',  'abstract', 'file', 'status')
    search_fields = ('id', 'title', 'author', 'abstract', 'file', 'status')
    list_filter = ('id', 'title', 'abstract', 'file', 'status')
    ordering = ('id', 'title', 'abstract', 'file', 'status')
    filter_horizontal = ()
    fieldsets = ()
