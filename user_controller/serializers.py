from rest_framework import serializers
from .models import SiteSettings, SkillSet


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
    username = serializers.CharField(required=True)


class SiteSettingSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteSettings
        fields = "__all__"


class SkillSetSerializer(serializers.ModelSerializer):

    class Meta:
        model = SkillSet
        fields = "__all__"
