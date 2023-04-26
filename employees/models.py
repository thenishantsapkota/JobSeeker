from django.conf import settings
from django.db import models

from employers.models import JobListing

# Create your models here.


class ApplicantProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    education = models.TextField()
    experience = models.TextField()
    skills = models.TextField()

    def __str__(self) -> str:
        return f"{self.user.username}'s profile"


class JobApplication(models.Model):
    job_listing = models.ForeignKey(JobListing, on_delete=models.CASCADE)
    applicant = models.ForeignKey(ApplicantProfile, on_delete=models.CASCADE)
    resume = models.FileField(upload_to="resumes/")
    cover_letter = models.TextField()
    date_applied = models.DateTimeField(auto_now_add=True)
    is_applied = models.BooleanField(default=True)
    is_reviewed = models.BooleanField(default=False)
    is_shortlisted = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["job_listing", "applicant"], name="unique_job_application"
            )
        ]

    def __str__(self) -> str:
        return f"{self.applicant.user.username} applied for {self.job_listing.position} at {self.job_listing.profile.company_name}"
