from django.contrib import admin
from .models import StudentUser, StudentPartnerPreferences, PartnerPreferences

class StudentPartnerPreferencesInline(admin.TabularInline):
    model = StudentPartnerPreferences
    extra = 1

@admin.register(StudentUser)
class StudentUserAdmin(admin.ModelAdmin):
    inlines = (StudentPartnerPreferencesInline,)

@admin.register(PartnerPreferences)
class PartnerPreferencesAdmin(admin.ModelAdmin):
    pass


