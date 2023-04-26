from django import forms

from employees.models import ApplicantProfile, JobApplication


class ApplicantProfileForm(forms.ModelForm):
    full_name = forms.CharField(
        max_length=255, widget=forms.TextInput({"placeholder": "Enter your full name"})
    )
    email = forms.CharField(
        max_length=255, widget=forms.TextInput({"placeholder": "Enter your email"})
    )
    phone_number = forms.CharField(
        max_length=20,
        widget=forms.TextInput({"placeholder": "Enter your phone number"}),
    )
    address = forms.CharField(
        max_length=255, widget=forms.TextInput({"placeholder": "Enter your address"})
    )
    education = forms.CharField(
        max_length=2500,
        widget=forms.Textarea(
            {
                "placeholder": "Enter your education details",
                "style": "height:200px;resize: none;",
            }
        ),
    )
    experience = forms.CharField(
        max_length=2500,
        widget=forms.Textarea(
            {
                "placeholder": "Enter your experience",
                "style": "height:200px;resize: none;",
            }
        ),
    )
    skills = forms.CharField(
        max_length=2500,
        widget=forms.Textarea(
            {"placeholder": "Enter your skills", "style": "height:200px;resize: none;"}
        ),
    )

    class Meta:
        model = ApplicantProfile
        fields = [
            "full_name",
            "email",
            "phone_number",
            "address",
            "education",
            "experience",
            "skills",
        ]


class JobApplyForm(forms.ModelForm):
    resume = forms.FileField(
        widget=forms.FileInput({"placeholder": "Upload your CV"}), required=True
    )
    cover_letter = forms.CharField(
        max_length=2500,
        widget=forms.Textarea({"placeholder": "Please write a short cover letter"}),
    )

    class Meta:
        model = JobApplication
        fields = ["resume", "cover_letter"]
