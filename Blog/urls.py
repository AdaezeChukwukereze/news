from django.urls import path
from .views import HomePage , DetailPage ,CreateNewsPage ,EditNewsPage,DeleteNewsPage

urlpatterns = [
    path("", HomePage.as_view(), name="home"),
    path("<int:pk>/" ,DetailPage.as_view(),name= "detail"),
    path("create/", CreateNewsPage.as_view(), name="create"),
    path("<int:pk>/edit/",EditNewsPage.as_view(), name="edit"),
    path("<int:pk>/delete", DeleteNewsPage.as_view(), name="delete")
]
