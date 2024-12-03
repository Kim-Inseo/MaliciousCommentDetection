from django.urls import path

from . import views

urlpatterns = [
    # /PredictApp/
    path('', views.input_data, name='input_data'),
    # /PredictApp/predict/
    path('predict/', views.predict_result, name='predict_result'),
]