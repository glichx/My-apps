from django.urls import path
from .views import *

urlpatterns = [
    path('',HomePageView.as_view(),name = "home"),
    # path('Update_profile/',User_InfoPageView.as_view(),name = "home"),
]