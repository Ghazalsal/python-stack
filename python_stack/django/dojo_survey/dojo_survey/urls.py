from django.urls import path, include
urlpatterns = [
    path('', include('survey_app.urls')),
]