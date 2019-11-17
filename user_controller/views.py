from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import APIException
from .serializers import *
from django.contrib.auth import get_user_model
from django.db.models import Q


class UserLogin(APIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data.get("email")
        password = serializer.validated_data.get("password")

        try:
            user = get_user_model().objects.get(
                Q(email=email) | Q(username=email)
            )
        except Exception:
            raise APIException("Invalid username or password")

        if not user.check_password(password):
            raise APIException("Invalid username or password")

        return Response(get_tokens_for_user(user), status=status.HTTP_200_OK)


class Register(APIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            get_user_model().objects._create_user(**serializer.validated_data)
        except Exception as e:
            raise APIException(e)

        return Response("User created successfully", status=status.HTTP_201_CREATED)


class SettingView(ListAPIView):
    queryset = SiteSettings.objects.all()
    serializer_class = SiteSettingSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class SkillSetView(ModelViewSet):
    queryset = SkillSet.objects.all()
    serializer_class = SkillSetSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


def get_tokens_for_user(user):
    token = RefreshToken.for_user(user)

    return {
        'access': str(token.access_token),
    }
