from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import (
    ApplicantRejectView,
    ApplicantShortlistView,
    ApplicantsView,
    CompanyProfileView,
    EmployerJobListingDeleteView,
    EmployerJobListingEditView,
    EmployerJobListingView,
    JobListingCreateView,
)

urlpatterns = [
    path(
        "company-profile/",
        login_required(CompanyProfileView.as_view(), login_url="/auth/login?next=/"),
        name="company-profile",
    ),
    path(
        "create-listing/",
        login_required(JobListingCreateView.as_view(), login_url="/auth/login?next=/"),
        name="create-listing",
    ),
    path(
        "listed-jobs/",
        login_required(
            EmployerJobListingView.as_view(), login_url="/auth/login?next=/"
        ),
        name="listed-jobs",
    ),
    path(
        "delete-job/<pk>/",
        login_required(
            EmployerJobListingDeleteView.as_view(), login_url="/auth/login?next=/"
        ),
        name="delete-job",
    ),
    path(
        "edit-job/<pk>/",
        login_required(
            EmployerJobListingEditView.as_view(), login_url="/auth/login?next=/"
        ),
        name="edit-job",
    ),
    path(
        "view-applicants/<pk>/",
        login_required(ApplicantsView.as_view(), login_url="/auth/login?next=/"),
        name="view-applicants",
    ),
    path(
        "shortlist-applicant/<pk>/",
        login_required(
            ApplicantShortlistView.as_view(), login_url="/auth/login?next=/"
        ),
        name="shortlist-applicant",
    ),
    path(
        "reject-applicant/<pk>/",
        login_required(ApplicantRejectView.as_view(), login_url="/auth/login?next=/"),
        name="reject-applicant",
    ),
]
