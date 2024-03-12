from django.urls import path, include
from .views import start_quiz,no_active_campaign,submit_quiz





urlpatterns = [
    path('start-quiz/', start_quiz, name='start_quiz'),
    path('submit-quiz/', submit_quiz, name='submit_quiz'),
    path('no-active-campaign/', no_active_campaign, name='no_active_campaign'),
]
