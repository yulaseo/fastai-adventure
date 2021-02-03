from rest_framework import serializers
from .models import Stock
from django.contrib.auth.models import AbstractUser,BaseUserManager

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbstractUser
        fields = ('email', 'username', 'active', 'admin', 'staff', 'confirmedEmail', 'dateRegistered')

class UserManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUserManager
        fields = ('email', 'username', 'password', 'is_active', 'is_admin', 'is_staff', 'confirmedEmail')     

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = (
            'company_name',
            'stock_code',
            'stock_type',
            'open',
            'high',
            'low',
            'close',
            'adj_close',
            'volume',
            'before_close',
            'increase',
            'decrease',
            'fluctuation_width',
            'bookmarked',
            'chart_image'
        )