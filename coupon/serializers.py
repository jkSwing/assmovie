from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from coupon.models import Coupon


class CouponSerializer(ModelSerializer):
    coupon_id = serializers.IntegerField(source='id')
    coupon_name = serializers.CharField(source='name')
    describe = serializers.StringRelatedField(source='cinema')
    time = serializers.DateTimeField(source='expire_time', format='%Y-%m-%d')

    class Meta:
        model = Coupon
        fields = ('coupon_id', 'coupon_name', 'describe', 'time')
