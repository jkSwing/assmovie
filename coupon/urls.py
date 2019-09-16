from django.urls import path
from coupon.views import get_coupons

coupon_urls = [
    path('', get_coupons),
]
