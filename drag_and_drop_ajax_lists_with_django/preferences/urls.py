from django.urls import include, path
from .views import StudentPartnerPreferencesReorder

urlpatterns = [
    path('preferences/<int:pk>/', StudentPartnerPreferencesReorder.as_view(), name='preferences'),
]
