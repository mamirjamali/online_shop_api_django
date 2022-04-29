from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreateSerializer


class UserCreateSerializer(BaseUserCreateSerializer):
    #Definig new object for creating User through the JWT authentication#
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password',
                  'email', 'first_name', 'last_name']


class UserSerializer(BaseUserSerializer):
    #Definig new object for User field on the JWT view#
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'email', 'username', 'first_name', 'last_name']
