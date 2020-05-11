from rest_framework import generics, mixins, status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import UserProfile
from .serializers import UserProfileSerializer

class UserProfileDetails(generics.GenericAPIView):
    """
    A Generic API View that gives Users complete information
    """
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        try:
            user_profile = UserProfile.objects.get(user=self.request.user)
        except:
            user_profile = None
        if not user_profile:
            return {'Error': 'Does Not Exists'}
        else:
            user_profile_data = {
                'user_id': user_profile.user.id,
                'first_name': user_profile.user.first_name,
                'last_name': user_profile.user.last_name,
                'email': user_profile.user.email,
                'id': user_profile.id,
                'bio': user_profile.bio,
                'age': user_profile.age,
                'telephone': user_profile.telephone_number,
                'location': user_profile.location,
                'birth_date': user_profile.birth_date
            }
        return user_profile_data

    def get(self, request, pk=None):
        return Response(self.get_queryset())

    def put(self, request, pk=None, format=None):
        user_profile_obj = UserProfile.objects.get(user=self.request.user)
        serializer = UserProfileSerializer(user_profile_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
