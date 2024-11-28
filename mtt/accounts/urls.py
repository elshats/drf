from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    AccountsListApiView,
    AccountsCreateApiView,
    AccountsDeleteView
)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='account-login'),
    path('login/refresh', TokenRefreshView.as_view(), name='account-refresh'),
    path('list/', AccountsListApiView.as_view(), name='account-list'),
    path('create/', AccountsCreateApiView.as_view(), name='account-create'),
    path('delete/', AccountsDeleteView.as_view({'delete': 'destroy'})),
]
