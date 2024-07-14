from django.contrib import admin
from.models import *
# Register your models here.

class BloodrequestAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'bloodgroup', 'quantity_ml', 'status', 'request_date')
    list_filter = ('status', 'bloodgroup')
    actions = ['approve_requests', 'reject_requests']

    def approve_requests(self, request, queryset):
        queryset.update(status='Approved')
    approve_requests.short_description = 'Approve selected requests'

    def reject_requests(self, request, queryset):
        queryset.update(status='Rejected')
    reject_requests.short_description = 'Reject selected requests'

class BloodDonationAdmin(admin.ModelAdmin):
    list_display = ('donor_name', 'blood_group', 'quantity_ml', 'status', 'donation_date')
    list_filter = ('status', 'blood_group')
    actions = ['approve_donations', 'reject_donations']

    def approve_donations(self, request, queryset):
        queryset.update(status='Approved')
    approve_donations.short_description = 'Approve selected donations'


    def reject_donations(self, request, queryset):
        queryset.update(status='Rejected')
    reject_donations.short_description = 'Reject selected donations'


admin.site.register(Bloodrequest,BloodrequestAdmin)
admin.site.register(BloodDonation,BloodDonationAdmin)
admin.site.register(MedicalProduct)
admin.site.register(Booking)
