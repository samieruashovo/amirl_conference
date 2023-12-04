from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Conference

# Register your models here.


@admin.register(Conference)
class ConferenceAdmin(admin.ModelAdmin):
    list_display = ['name', 'acronym', 'description', 'thumbnail', 'submission_start',
                    'submission_deadline', 'conference_date', 'created_at', 'place', 'website']
    list_filter = ['name', 'acronym']
