from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views import View

from employees.models import JobApplication

from .forms import CompanyProfileForm, JobListingForm
from .models import CompanyProfile, JobListing

# Create your views here.


class CompanyProfileView(View):
    form = CompanyProfileForm

    def get(self, request: HttpRequest):
        if request.user.is_user:
            return redirect("home")
        profile = CompanyProfile.objects.filter(user_id=request.user.id)
        if profile.exists():
            form = self.form(instance=profile.first())
        else:
            form = self.form()

        return render(request, "employers/company_profile.html", context={"form": form})

    def post(self, request: HttpRequest):
        form = self.form(request.POST)
        if form.is_valid():
            profile = CompanyProfile.objects.filter(user_id=request.user.id)
            if profile.exists():
                model = profile.first()
                model.company_name = form.data.get("company_name")
                model.company_email = form.data.get("company_email")
                model.company_website = form.data.get("company_website")
                model.company_bio = form.data.get("company_bio")
                model.save()
            else:
                company_profile = form.save(commit=False)
                company_profile.is_complete = True
                company_profile.user_id = request.user.id
                company_profile.save()
            messages.success(request, "Profile saved successfully!")
            return redirect("home")
        return render(request, "employers/company_profile.html", context={"form": form})


class JobListingCreateView(View):
    form = JobListingForm

    def get(self, request: HttpRequest):
        if request.user.is_user:
            return redirect("home")
        form = self.form()
        profile = CompanyProfile.objects.filter(user_id=request.user.id)
        if profile.exists():
            return render(request, "employers/list_job.html", context={"form": form})
        messages.error(request, "Profile not setup")
        return redirect("home")

    def post(self, request: HttpRequest):
        form = self.form(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.profile = request.user.companyprofile
            job.save()
            messages.success(
                request, "Job listing submitted for verification successfully!"
            )
            return redirect("listed-jobs")
        return render(request, "employers/list_job.html", context={"form": form})


class EmployerJobListingView(View):
    def get(self, request: HttpRequest):
        if request.user.is_user:
            return redirect("home")
        profile = CompanyProfile.objects.filter(user_id=request.user.id)
        if profile.exists():
            jobs = JobListing.objects.filter(
                profile_id=request.user.companyprofile.id
            ).all()
            return render(request, "employers/listed_jobs.html", context={"jobs": jobs})
        messages.error(request, "Profile not setup")
        return redirect("home")


class EmployerJobListingDeleteView(View):
    def get(self, request: HttpRequest, pk):
        if request.user.is_user:
            return redirect("home")
        job = JobListing.objects.filter(
            id=pk, profile_id=request.user.companyprofile.id
        ).first()
        if job:
            job.delete()
            messages.success(request, "Job listing deleted successfully!")
            return redirect("listed-jobs")
        return render(request, "employers/404.html", status=404)


class ApplicantsView(View):
    def get(self, request, pk):
        job = JobListing.objects.filter(id=pk).first()
        if not job:
            return render(request, "employers/404.html", status=404)
        if request.user.companyprofile != job.profile:
            return render(request, "employers/404.html", status=404)
        applicants = JobApplication.objects.filter(job_listing_id=pk).all()
        return render(
            request,
            "employers/applicants.html",
            context={"applicants": applicants, "job": job},
        )


class EmployerJobListingEditView(View):
    form = JobListingForm

    def get(self, request: HttpRequest, pk):
        if request.user.is_user:
            return redirect("home")
        job = JobListing.objects.filter(
            id=pk, profile_id=request.user.companyprofile.id
        )
        form = self.form(instance=job.first())
        return render(request, "employers/list_job.html", context={"form": form})

    def post(self, request: HttpRequest, pk):
        form = self.form(request.POST)
        job = JobListing.objects.filter(
            id=pk, profile_id=request.user.companyprofile.id
        ).first()
        if job and form.is_valid() and request.user.companyprofile.id == job.profile_id:
            job.position = form.data.get("position")
            job.salary = form.data.get("salary")
            job.experience = form.data.get("experience")
            job.job_description = form.data.get("job_description")
            job.type = form.data.get("type")
            job.save()
            messages.success(request, "Job updated!")
            return redirect("listed-jobs")
        return render(request, "employers/list_job.html", context={"form": form})


class ApplicantShortlistView(View):
    def get(self, request, pk):
        application = JobApplication.objects.filter(id=pk).first()
        if request.user.companyprofile != application.job_listing.profile:
            return render(request, "employers/404.html", status=404)
        if application:
            application.is_shortlisted = not application.is_shortlisted
            application.save()
            return redirect("view-applicants", pk=application.job_listing_id)
        return redirect("listed-jobs")


class ApplicantRejectView(View):
    def get(self, request, pk):
        application = JobApplication.objects.filter(id=pk).first()
        if request.user.companyprofile != application.job_listing.profile:
            return render(request, "employers/404.html", status=404)
        if application:
            application.is_rejected = not application.is_rejected
            application.save()
            return redirect("view-applicants", pk=application.job_listing_id)
        return redirect("listed-jobs")
