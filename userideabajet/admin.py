from django.contrib import admin
from .models import UserSubmission, SubmissionDetail


@admin.register(UserSubmission)
class UserSubmissionAdmin(admin.ModelAdmin):
    # Displayed columns in the admin list view
    list_display = (
        'name',
        'submission_id',
        'name',
        'email',
        'status',
        'submission_date'
    )

    # Filters on the right side
    list_filter = (
        'status',
        'submission_date',
        'jantina',
        'bangsa',
        'umur',
        'job',
        'zon'
    )

    # Search bar fields
    search_fields = (
        'name',
        'email',
        'cad'
    )

    # Fields that cannot be edited
    readonly_fields = (
        'submission_id',
        'submission_date'
    )

    # Organizing fields into sections
    fieldsets = (
        ('User Information', {
            'fields': ('name', 'email', 'jantina', 'bangsa', 'umur', 'job', 'zon', 'submission_date')
        }),
        ('Project Details', {
            'fields': ('cad',)
        }),
        ('Additional Information', {
            'fields': ('status',)
        }),
    )


@admin.register(SubmissionDetail)
class SubmissionDetailAdmin(admin.ModelAdmin):
    list_display = (
        'submission',
        'element_number',
        'pilihan',
        'lokasi',
        'butiran'
    )
    list_filter = (
        'element_number',
        'lokasi'
    )
    search_fields = (
        'submission__name',
        'pilihan',
        'lokasi',
        'butiran'
    )
