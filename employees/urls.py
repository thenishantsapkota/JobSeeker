from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import (
    ApplicantProfileEditView,
    ApplicantProfileView,
    JobApplyView,
    JobDetailView,
    JobListingView,
    MyApplicationsView,
)

urlpatterns = [
    path(
        "my-applications/",
        login_required(MyApplicationsView.as_view(), login_url="/auth/login?next=/"),
        name="my-applications",
    ),
    path(
        "job-listings/",
        login_required(JobListingView.as_view(), login_url="/auth/login?next=/"),
        name="job-listings",
    ),
    path(
        "applicant-profile/",
        login_required(ApplicantProfileView.as_view(), login_url="/auth/login?next=/"),
        name="applicant-profile",
    ),
    path(
        "edit-applicant-profile/",
        login_required(
            ApplicantProfileEditView.as_view(), login_url="/auth/login?next=/"
        ),
        name="edit-applicant-profile",
    ),
    path(
        "job-detail/<pk>/",
        login_required(JobDetailView.as_view(), login_url="/auth/login?next=/"),
        name="job-detail",
    ),
    path(
        "job-apply/<pk>",
        login_required(JobApplyView.as_view(), login_url="/auth/login?next=/"),
        name="job-apply",
    ),
]
