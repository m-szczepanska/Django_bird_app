from django.urls import path
from . import views

urlpatterns = [
    path('trial/', views.trial_function, name='trial')

]
