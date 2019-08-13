from rest_framework import serializers
from rest_framework.serializers import ValidationError
from .models import AssetType, Assets, Tickets, Distributor, PaymentType, Payments, Priorities, Rolemapping, Roles, Supplier, TicketStatus, Users 
from django.core.validators import validate_email


class AssetTypeSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Chain model """
    class Meta:
        model = AssetType
        exclude=('created_date','updated_date','created_by','updated_by')

class AssetsSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Chain model """
    class Meta:
        model = Assets
        exclude=('created_date','updated_date','created_by','updated_by')

class TicketsSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Chain model """
    class Meta:
        model = Tickets
        exclude=('created_date','updated_date','created_by','updated_by')

class DistributorSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Chain model """
    class Meta:
        model = Distributor
        exclude=('created_date','updated_date','created_by','updated_by')

class PaymentTypeSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Chain model """
    class Meta:
        model = PaymentType
        exclude=('created_date','updated_date','created_by','updated_by')

class PaymentsSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Chain model """
    class Meta:
        model = Payments
        exclude=('created_date','updated_date','created_by','updated_by')

class PrioritiesSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Chain model """
    class Meta:
        model = Priorities
        exclude=('created_date','updated_date','created_by','updated_by')

class UsersSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Chain model """
    # password = serializers.CharField( write_only=False, required=True,
    #     style={'input_type': 'password', 'placeholder': 'Password'}
    # )
    # cnfpassword = serializers.CharField( write_only=False, required=True, label='Confirm Password',
    #     style={'input_type': 'password', 'placeholder': 'Confirm Password'}
    # )
    class Meta:
        model = Users
        exclude=('created_date','updated_date','created_by','updated_by')
        extra_kwargs = {"cnfpassword":{"write_only":True},"password":{"write_only":True}}
        

    def validate_password(self,value):
        data = self.get_initial()
        password = value
        cnfpassword = data.get('cnfpassword')
        print(password,cnfpassword)
        if(password != cnfpassword):
            raise ValidationError('Passwords must match')
        return value

    def validate_cnfpassword(self,value):
        data = self.get_initial()
        password = data.get('password')
        cnfpassword = value
        print(password,cnfpassword)
        if(password != cnfpassword):
            raise ValidationError('Passwords must match')
        return value


class TicketStatusSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Chain model """
    class Meta:
        model = TicketStatus
        exclude=('created_date','updated_date','created_by','updated_by')

class RolemappingSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Chain model """
    class Meta:
        model = Rolemapping
        exclude=('created_date','updated_date','created_by','updated_by')

class RolesSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Chain model """
    class Meta:
        model = Roles
        exclude=('created_date','updated_date','created_by','updated_by')

class SupplierSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Chain model """
    class Meta:
        model = Supplier
        exclude=('created_date','updated_date','created_by','updated_by')

