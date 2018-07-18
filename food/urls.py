from django.urls import path
from . import views

app_name = "food"

urlpatterns = [
    path("create/", views.CreateFood.as_view(), name="create"),
    path("detail/<int:pk>/", views.FoodDetail.as_view(), name="detail"),
    path("list/", views.FoodList.as_view(), name="list"),
    path("update/<int:pk>/", views.UpdateFood.as_view(), name="update"),
    path("delete/<int:pk>/", views.DeleteFood.as_view(), name="delete"),
    path("delete/success.html", views.success_delete_food, name="success_delete"),

    path("deposit/<int:food_id>/", views.IncreaseReserves.as_view(), name='increase_reserves'),
    path("deposit/success/<int:food_id>/", views.success_increase_reserves, name='success_increase_reserve'),

    path('unit/list/', views.DistributionUnitList.as_view(), name='unit_list'),
    path('unit/detail/<int:pk>/', views.DistributionUnitDetail.as_view(), name='unit_detail'),
    path('unit/create/', views.CreateDistributionUnit.as_view(), name='unit_create'),
    path('unit/update/<int:id>/', views.UpdateDistributionUnit.as_view(), name='unit_update'),
    path('unit/delete/<int:pk>/', views.DeleteDistributionUnit.as_view(), name='unit_delete'),
    path('unit/delete/success.html', views.success_delete_food_unit, name='success_delete_unit')
]