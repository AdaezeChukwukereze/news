from django.urls import path
from .views import api_list_page ,Api_list_page,api_detail_view,api_create_page,api_update_page

urlpatterns=[
    path("home/", api_list_page, name="api-home"),
    path("class/home/", Api_list_page.as_view(),name="Api-home"),
    path("class/detail/<slug:slug>/", api_detail_view.as_view(), name="class-detail"),
    path("create/", api_create_page, name="api-create"),
    path("<slug:slug>/update",api_update_page,name="update")
]