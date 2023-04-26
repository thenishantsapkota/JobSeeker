from django.contrib import admin

from .models import CompanyProfile, JobListing


@admin.register(JobListing)
class JobListingAdmin(admin.ModelAdmin):
    list_display = (
        "position",
        "profile",
        "type",
        "experience",
        "salary",
        "is_approved",
    )
    list_filter = ("profile__company_name", "type", "experience", "is_approved")
    search_fields = ("position", "job_description", "profile__company_name")
    readonly_fields = ("profile",)
    fieldsets = (
        (None, {"fields": ("position", "type", "experience", "job_description")}),
        ("Company Profile", {"fields": ("profile",), "classes": ("collapse",)}),
        ("Salary and Approval", {"fields": ("salary", "is_approved")}),
    )
