from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Review

# Register your models here.


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'reviewer', 'paper', 'score', 'comment')
    search_fields = ('id', 'reviewer', 'paper', 'score', 'comment')
    list_filter = ('id', 'reviewer', 'paper', 'score', 'comment')
    ordering = ('id', 'reviewer', 'paper', 'score', 'comment')
    filter_horizontal = ()
    fieldsets = ()
