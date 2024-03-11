import csv
from django.http import HttpResponse
from django.contrib import admin
from .models import Profile

# Export to CSV Action
def export_to_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="export.csv"'
    writer = csv.writer(response)
    writer.writerow([field.name for field in modeladmin.model._meta.get_fields()])

    for obj in queryset:
        row = [getattr(obj, field.name, None) for field in modeladmin.model._meta.get_fields()]
        writer.writerow(row)
    return response

export_to_csv.short_description = 'Download selected as CSV'

# Admin model for Profile
class ProfileAdmin(admin.ModelAdmin):
    actions = [export_to_csv]

admin.site.register(Profile, ProfileAdmin)
