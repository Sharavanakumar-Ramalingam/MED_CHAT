from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page URL
    path('predict_disease/', views.predict_disease, name='predict_disease'),  # Prediction endpoint URL
]
