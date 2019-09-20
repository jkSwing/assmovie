from rest_framework.response import Response
from rest_framework.decorators import api_view
from user.models import User
from hashlib import sha256
import uuid


def get_hashed_pwd(password, salt=None):
    if not salt:
        salt = uuid.uuid4().hex
    sh = sha256((password + salt).encode())
    return sh.hexdigest(), salt


@api_view(['POST'])
def login(request):
    # user_id = request.session.get('user_id')
    # print(user_id)
    username = request.POST.get('username')
    password = request.POST.get('password')
    if not username or not password:
        return Response({'success': False, 'message': 'shit'})
    try:
        user = User.objects.get(name=username)
    except User.DoesNotExist:
        return Response({'success': False, 'message': '用户名或密码错误'})
    salted_pwd, _ = get_hashed_pwd(password, user.salt)
    if salted_pwd != user.password:
        return Response({'success': False, 'message': '用户名或密码错误'})

    request.session['user_id'] = user.id
    return Response({'success': True, 'message': '登录成功'})


@api_view(['POST'])
def register(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if not username or not password:
        return Response({'success': False, 'message': 'shit'})
    if User.objects.filter(name=username).exists():
        return Response({'success': False, 'message': '用户名重复'})
    user = User()
    user.name = username
    user.password, user.salt = get_hashed_pwd(password)
    user.save()

    return Response({'success': True, 'message': '注册成功'})
