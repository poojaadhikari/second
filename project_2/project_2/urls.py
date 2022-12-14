
from django.contrib import admin
from django.urls import path
from project_APP import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signinView)
]
