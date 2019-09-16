from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime
from coupon.models import Coupon
from coupon.serializers import CouponSerializer


@api_view(['GET'])
def get_coupons(request):
    user_id = request.GET.get('user_id')
    expired = request.GET.get('expired')
    page = request.GET.get('page')
    limit = request.GET.get('limit')
    if not user_id:
        return Response({'success': False, 'message': '...'})

    if not page:
        page = 1
    if not limit:
        limit = 5
    page = int(page)
    limit = int(limit)
    start = (page - 1) * limit
    if not expired:
        coupons = Coupon.objects.filter(user_id=user_id, expire__time__gte=datetime.now()).order_by('expire_time')[start: start + limit]
    else:
        coupons = Coupon.objects.filter(user_id=user_id).order_by('expire_time')[start: start + limit]
    serializer = CouponSerializer(coupons, many=True)

    return Response({'success': True, 'message': '成功', 'data': serializer.data})
