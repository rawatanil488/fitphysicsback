from .serializers import UserSerializer
from .models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, mixins


class UserProfileViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    A viewset that provides the standard GET action for Profile Endpoint
    """
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = User.objects.filter(id=self.request.user.id)
        return user
