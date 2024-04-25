# urls.py
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from nxtbn.users.api.v1.views import CustomTokenObtainPairView, SignupView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'), # login
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
