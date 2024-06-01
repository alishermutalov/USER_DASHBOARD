from django.urls import path
from .views import UserAccountListView, CustomUserUpdateView,\
    HomeView, RegisterView, CustomLoginView, user_logout, CustomPasswordChangeView,\
    password_change_done


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('profile/', UserAccountListView.as_view(), name='profile'),
    path('profile/update/', CustomUserUpdateView.as_view(), name='update_url'),
    path('register/', RegisterView.as_view(), name='register'),
    path('password/change/', CustomPasswordChangeView.as_view(), name='change_password'),
    path('login/', CustomLoginView.as_view(), name='login'),
    
    path('password/change/done', password_change_done, name='password_change_done'),
    path('logout/', user_logout, name='logout'),
]