from django.urls import path
from . import views

urlpatterns = [

    path('', views.dashboard, name='dashboard'),

    path('login/', views.login_view, name='panel_login'),

    path('logout/', views.logout_view, name='panel_logout'),

    path('panel/<str:model_name>/', views.item_list, name='panel_item_list'),
    path('panel/<str:model_name>/add/', views.item_create, name='panel_item_create'),
    path('panel/<str:model_name>/<int:pk>/edit/', views.item_update, name='panel_item_update'),
    path('panel/<str:model_name>/<int:pk>/delete/', views.item_delete, name='panel_item_delete'),

]

