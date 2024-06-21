from django.urls import path

from . import views

app_name = 'lmnp'


urlpatterns = [
    path('preview', views.PreviewConfig.as_view(), name='preview_config'),
]
