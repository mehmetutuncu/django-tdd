from django.urls import path
from . import views
app_name = 'testapi'

urlpatterns = [
    path('login', views.login, name='login')
]