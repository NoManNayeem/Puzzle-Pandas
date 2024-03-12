from django.urls import path
from .views.loginView import login_view
from .views.registerView import register_view
from .views.homeView import home_view
from .views.logoutView import custom_logout_view  # Make sure to import your custom logout view
from .views.landingView import landing_page_view





urlpatterns = [
    path('', landing_page_view, name='landing_page'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('home/', home_view, name='home'),
    path('logout/', custom_logout_view, name='logout'),  # Use your custom logout view
]
