from rest_framework import serializers
from .models import Cupom
from user.models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'type', 'phone', 'city', 'uf', 'pix', 'image', 'site', 'name']
        extra_kwargs = {'password': {'write_only': True}}

class CupomSerializer(serializers.ModelSerializer):
    expiration = serializers.DateTimeField(required=False)
    owner = UserSerializer() 
    
    class Meta:
        model = Cupom
        fields = ['id', 'value', 'description', 'expiration', 'image', 'owner', 'is_active']
        read_only_fields = ['owner', 'is_active']

class CupomUpdateSerializer(serializers.ModelSerializer):
    expiration = serializers.DateTimeField(required=False) 
    owner = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), required=False) 
    
    class Meta:
        model = Cupom
        fields = ['id', 'value', 'description', 'expiration', 'image', 'owner', 'is_active']
        read_only_fields = ['owner', 'is_active']

    def update(self, instance, validated_data):
        # Verifica se uma nova imagem foi fornecida na requisição
        new_image = validated_data.get('image', None)
        if new_image:
            # Se uma nova imagem foi fornecida, apaga a imagem antiga se existir
            if instance.image:
                instance.image.delete()
        
        return super().update(instance, validated_data)