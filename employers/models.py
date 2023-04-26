from django.db import models


# Create your models here.
class CompanyProfile(models.Model):
    user = models.OneToOneField(
        "authentication.CustomUser", on_delete=models.CASCADE, null=True
    )
    company_name = models.CharField(max_length=100)
    company_email = models.EmailField()
    company_website = models.CharField(max_length=100)
    company_bio = models.TextField()
    is_complete = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.company_name}"


class JobListing(models.Model):
    profile = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    job_description = models.TextField()
    salary = models.FloatField(null=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.position}-{self.profile.company_name}"
