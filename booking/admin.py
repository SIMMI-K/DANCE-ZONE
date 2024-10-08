from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import DanceClass , DanceBooking

# Register your models here.
@admin.register(DanceClass)
class DanceClassAdmin(SummernoteModelAdmin):

    summernote_fields = ("content",)


@admin.register(DanceBooking)
class DanceBookingAdmin(admin.ModelAdmin):
    """Class to view the Bookings in the admin panel"""

    list_display = (
        "username",
        "date_of_booking",
        "dance_style",
        "start_time",
        "confirmed",
    )
    list_filter = ("date_of_booking", "username")
    search_fields = ["username", "dance_style"]
    actions = ["confirm_booking"]

    def confirm_booking(self, request, queryset):
        queryset.update(confirmed=True)