from rest_framework.serializers import ModelSerializer
from .models import NewUser, Profile


class RegisterUserSerializer(ModelSerializer):
    class Meta:
        model = NewUser
        fields = ('email', 'password', 'first_name', 'last_name', 'user_name')

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id','name', 'maturity_setting', 'user','image')
