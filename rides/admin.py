from django.contrib import admin
from .models import RideRequest

@admin.register(RideRequest)
class RideRequestAdmin(admin.ModelAdmin):
    list_display = (
        'request_id', 
        'creator', 
        'creator_type',
        'start_location',
        'destination_location',
        'start_time',
        'end_time',
        'status',
        'created_at'
    )
    list_filter = ('creator_type', 'status', 'created_at')
    search_fields = (
        'request_id',
        'creator__username',
        'creator__email',
        'start_location',
        'destination_location'
    )
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('creator', 'creator_type', 'status', 'note')
        }),
        ('Locations', {
            'fields': (
                ('start_location', 'start_latitude', 'start_longitude'),
                ('destination_location', 'destination_latitude', 'destination_longitude')
            )
        }),
        ('Time Information', {
            'fields': (('start_time', 'end_time'), ('created_at', 'updated_at'))
        }),
    ) 