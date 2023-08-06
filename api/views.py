from rest_framework import generics, permissions
from .models import Rocket
from .serializers import RocketSerializer


from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class RocketList(generics.ListAPIView):
    serializer_class = RocketSerializer

    def get_queryset(self):
        queryset = Rocket.objects.all()
        return queryset

class RocketDetail(generics.RetrieveAPIView):
    serializer_class = RocketSerializer
    queryset = Rocket.objects.all()

class RocketCreate(generics.CreateAPIView):
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = RocketSerializer
    queryset = Rocket.objects.all()

class RocketEdit(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = RocketSerializer
    queryset = Rocket.objects.all()

class RocketDelete(generics.RetrieveDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = RocketSerializer
    queryset = Rocket.objects.all()