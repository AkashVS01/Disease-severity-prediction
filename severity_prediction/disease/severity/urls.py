from django.urls import path

from . import views

urlpatterns = [
    
    path('',views.home, name="home"),
    path('find_disease/', views.find_disease, name="find_disease"),
    path('store_data/', views.store_data, name="store_data"),
    
    path('cardio_severity/',views.cardio_severity,name="cardio_severity"),
    path('cardio_disease/',views.cardio_disease,name="cardio_disease"),

    path('jaundice_severity/',views.jaundice_severity,name="jaundice_severity"),
    path('jaundice_disease/',views.jaundice_disease,name="jaundice_disease"),

    path('allergy_severity/',views.allergy_severity,name="allergy_severity"),
    path('allergy_disease/',views.allergy_disease,name="allergy_disease"),

    path('cold_severity/',views.cold_severity,name="cold_severity"),
    path('cold_disease/',views.cold_disease,name="cold_disease"),

    path('diabetes_severity/',views.diabetes_severity,name="diabetes_severity"),
    path('diabetes_disease/',views.diabetes_disease,name="diabetes_disease"),

    path('thyroid_severity/',views.thyroid_severity,name="thyroid_severity"),
    path('thyroid_disease/',views.thyroid_disease,name="thyroid_disease"),

    path('hepatitis_severity/',views.hepatitis_severity,name="hepatitis_severity"),
    path('hepatitis_disease/',views.hepatitis_disease,name="hepatitis_disease"),
]

