from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("", views.index, name= "home"),
    path("log_in", views.log_in, name= "log_in"),
    path("register", views.register, name= "register"),
    path("dashboard", views.dashboard, name= "dashboard"),
    path("hr_dashboard", views.hr_dashboard, name= "hr_dashboard"),
    path("create_job", views.create_job, name= "create_job"),
    path("log_out", views.log_out, name= "log_out"),
    path("result", views.result, name= "result"),
]
