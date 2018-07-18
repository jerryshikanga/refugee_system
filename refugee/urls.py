from django.urls import path
from . import views

app_name = "refugee"

urlpatterns = [
    path("create/", views.CreateRefugee.as_view(), name="create"),
    path("detail/<int:pk>/", views.RefugeeDetail.as_view(), name="detail"),
    path("list/", views.RefugeeList.as_view(), name="list"),
    path("list/pdf/generate/", views.refugee_list_pdf, name="list_pdf"),
    path("update/<int:pk>/", views.UpdateRefugee.as_view(), name="update"),
    path("delete/<int:pk>/", views.DeleteRefugee.as_view(), name="delete"),
    path("delete/success.html", views.success_delete_refugee, name="success_delete"),
]