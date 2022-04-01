from rest_framework import serializers
from .models import MailingList, User, Organization

class MailSerializer(serializers.ModelSerializer):
     class Meta:
        model = MailingList
        fields = ['name', 'email']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class HardRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  ['name', 'email', 'password', 'role', 'Individual', 'pan', 'aadhar', 'bank_proof', 'cancelled_cheque', 'CRM_report', 'demat', 'tan', 'gst', 'transaction_type']
        extra_kwargs = {
            'password': {'write_only': True}
        }
