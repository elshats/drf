from rest_framework import generics, permissions, status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .serializers import AccountsSerializer
from .models import Accounts

from common.permissions import (
    IsAdmin
)


class AccountsListApiView(generics.ListAPIView):
    permission_classes = [
        permissions.AllowAny
    ]
    queryset = Accounts.objects.all()
    serializer_class = AccountsSerializer


class AccountsCreateApiView(generics.CreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
        IsAdmin
    ]

    queryset = Accounts.objects.all()
    serializer_class = AccountsSerializer


class AccountsDeleteView(ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
        IsAdmin
    ]

    def destroy(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id', None)

        if user_id:
            Accounts.objects.get(id=user_id).delete()
            return Response(status=status.HTTP_200_OK, data={'message': 'Пользователь успешно удален'})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': 'Id пользователя не указан'})
