from django.contrib import admin
from django.urls import path, include
from nxtbn.core.api.v1 import views

urlpatterns = [
    path('core/', views.TemplateUploadAPIView.as_view(), name='tempalte_upload'),
]
