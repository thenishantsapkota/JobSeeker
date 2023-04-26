from django import forms

from .models import CompanyProfile, JobListing

JOB_CHOICES = (
    ("intern", "Internship"),
    ("onsite", "On Site"),
    ("remote", "Remote"),
    ("hybrid", "Hybrid"),
)


class CompanyProfileForm(forms.ModelForm):
    company_name = forms.CharField(
        max_length=100, widget=forms.TextInput({"placeholder": "Enter company name"})
    )
    company_email = forms.CharField(
        max_length=100, widget=forms.TextInput({"placeholder": "Enter company email"})
    )
    company_website = forms.CharField(
        max_length=100, widget=forms.TextInput({"placeholder": "Enter company website"})
    )
    company_bio = forms.CharField(
        max_length=2500,
        required=True,
        widget=forms.Textarea(
            {
                "placeholder": "Enter your company bio",
                "style": "height:200px;",
            }
        ),
    )

    class Meta:
        model = CompanyProfile
        fields = ["company_name", "company_email", "company_website", "company_bio"]


class JobListingForm(forms.ModelForm):
    position = forms.CharField(
        max_length=100,
        widget=forms.TextInput({"placeholder": "Enter designated position"}),
    )
    type = forms.Field(
        widget=forms.Select(
            {"placeholder": "Select job type"},
            choices=JOB_CHOICES,
        )
    )
    experience = forms.CharField(
        max_length=100,
        widget=forms.TextInput({"placeholder": "Enter required experience"}),
    )
    salary = forms.FloatField(
        widget=forms.TextInput({"placeholder": "Enter approx. salary"})
    )
    job_description = forms.CharField(
        max_length=2500,
        widget=forms.Textarea(
            {
                "placeholder": "Enter Job Description",
                "style": "height:200px;",
            }
        ),
    )

    class Meta:
        model = JobListing
        fields = ["position", "type", "experience", "job_description", "salary"]
