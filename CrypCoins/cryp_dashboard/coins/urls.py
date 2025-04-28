from django.urls import include,path
from . import views
from cryp_dashboard import coins

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
]
