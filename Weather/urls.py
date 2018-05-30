from django.urls import path
from Weather import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='home')
]
