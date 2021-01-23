from django.urls import path
from .views import HomepageView

urlpatterns = [

    path("", HompageView.as_view(), name="home"),
]