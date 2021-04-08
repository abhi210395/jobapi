
from django.urls import path
from jobs.api.views import JobCreateAPIView,JobDetailAPIView

urlpatterns = [
    path('jobs/', JobCreateAPIView.as_view(),name = "job-list"),
    path('jobs/<int:pk>/', JobDetailAPIView.as_view(),name = "job-detail"),
]
