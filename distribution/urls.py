from django.urls import path
from . import views

app_name = "distribution"

urlpatterns = [
    path("allocate/<int:food_id>/", views.allocate_distribution, name='allocate_distribution'),
    path("list/", views.DistributionList.as_view(), name='list'),

    path("clear/<int:distribution_id>/", views.clear_distribution, name="clear"),
    path("cleared/pdf/generate/<int:distribution_id>/", views.cleared_distribution_pdf, name="cleared_pdf"),
]