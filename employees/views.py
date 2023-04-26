from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View

from employers.models import JobListing

from .forms import ApplicantProfileForm, JobApplyForm
from .models import ApplicantProfile, JobApplication


# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(request, "employees/home.html")


class ApplicantProfileView(View):
    form = ApplicantProfileForm

    def get(self, request):
        profile = ApplicantProfile.objects.filter(user_id=request.user.id).first()
        if profile:
            return render(
                request, "employees/profile.html", context={"profile": profile}
            )
        form = self.form()
        return render(
            request, "employees/applicant_profile.html", context={"form": form}
        )

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, "Applicant profile updated!")
            return redirect("home")
        return render(
            request, "employees/applicant_profile.html", context={"form": form}
        )


class ApplicantProfileEditView(View):
    form = ApplicantProfileForm

    def get(self, request):
        profile = ApplicantProfile.objects.filter(user_id=request.user.id).first()
        if profile:
            form = self.form(instance=profile)
            return render(
                request, "employees/applicant_profile.html", context={"form": form}
            )
        messages.error(request, "Applicant profile not setup")
        return redirect("home")

    def post(self, request):
        form = self.form(request.POST)
        profile = ApplicantProfile.objects.filter(user_id=request.user.id).first()
        if profile:
            profile.full_name = form.data.get("full_name")
            profile.email = form.data.get("email")
            profile.phone_number = form.data.get("phone_number")
            profile.address = form.data.get("address")
            profile.education = form.data.get("education")
            profile.experience = form.data.get("experience")
            profile.skills = form.data.get("experience")

            profile.save()
            messages.success(request, "Applicant profile updated!")
            return redirect("applicant-profile")
        return render(
            request, "employees/applicant_profile.html", context={"form": form}
        )


class MyApplicationsView(View):
    def get(self, request):
        profile = ApplicantProfile.objects.filter(user_id=request.user.id).first()
        if profile:
            job_applications = JobApplication.objects.filter(applicant=profile).all()
            return render(
                request,
                "employees/applications.html",
                context={"applications": job_applications},
            )
        messages.error(request, "Applicant profile not setup")
        return redirect("home")


class JobListingView(View):
    def get(self, request):
        profile = ApplicantProfile.objects.filter(user_id=request.user.id).first()
        if profile:
            applications = JobApplication.objects.filter(
                applicant=request.user.applicantprofile
            )
            applied_jobs = [app.job_listing for app in applications]
            jobs = JobListing.objects.filter(is_approved=True).all()
            return render(
                request,
                "employees/listings.html",
                context={"jobs": jobs, "applications": applied_jobs},
            )
        messages.error(request, "Applicant profile not setup")
        return redirect("home")


class JobDetailView(View):
    def get(self, request, pk):
        profile = ApplicantProfile.objects.filter(user_id=request.user.id).first()
        job = JobListing.objects.filter(id=pk).first()
        if job and profile:
            return render(request, "employees/job_detail.html", context={"job": job})
        return redirect("home")


class JobApplyView(View):
    form = JobApplyForm

    def get(self, request, pk):
        form = self.form()
        profile = ApplicantProfile.objects.filter(user_id=request.user.id).first()
        job = JobListing.objects.filter(id=pk).first()
        if job and profile:
            return render(
                request,
                "employees/job_apply.html",
                context={
                    "form": form,
                    "job": job,
                },
            )
        return redirect("home")

    def post(self, request, pk):
        form = self.form(request.POST, request.FILES)
        job = JobListing.objects.filter(id=pk).first()
        if not job:
            return redirect("job-listings")
        if form.is_valid():
            job_application = form.save(commit=False)
            job_application.applicant = request.user.applicantprofile
            job_application.job_listing = job
            job_application.save()
            messages.success(request, f"Applied for {job.position} successfully!")
            return redirect("my-applications")
        return render(request, "employees/job_apply.html", context={"form": form})
