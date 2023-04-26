# from django.contrib import admin

# from .models import ApplicantProfile, JobApplication


# @admin.register(ApplicantProfile)
# class ApplicantProfileAdmin(admin.ModelAdmin):
#     list_display = [
#         "full_name",
#         "email",
#         "phone_number",
#         "address",
#         "education",
#         "experience",
#         "skills",
#     ]
#     search_fields = ["full_name", "email"]
#     readonly_fields = ("user",)


# @admin.register(JobApplication)
# class JobApplicationAdmin(admin.ModelAdmin):
#     list_display = [
#         "job_listing",
#         "applicant",
#         "resume",
#         "date_applied",
#         "is_reviewed",
#         "is_shortlisted",
#         "is_rejected",
#     ]
#     search_fields = [
#         "applicant__full_name",
#         "job_listing__position",
#         "job_listing__profile__company_name",
#     ]
#     readonly_fields = ("applicant",)
