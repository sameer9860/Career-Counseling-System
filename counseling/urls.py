from django.urls import path

from . import views

urlpatterns = [
    path("", views.counseling_form, name="counseling_form"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("report/<int:student_id>/", views.generate_pdf, name="generate_pdf"),
]

