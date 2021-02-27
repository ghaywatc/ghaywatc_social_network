from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



app_name= 'accounts'

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('Signup/',views.Signup.as_view(),name='signup'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]